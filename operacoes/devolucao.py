from datetime import datetime
from operacoes.locacao import lista_locacoes
from operacoes.cadastro import estoque_carros
from utilidades.interface import cabecalho
from utilidades.calculos import formatar_moeda, calcular_multa_km, calcular_multa_atraso
from utilidades import banco_dados

def realizar_devolucao():
    cabecalho('DEVOLUÇÃO DE VEÍCULO')

    placa_busca = input('Digite a placa do veículo: ')
    contrato_atual = None
    for contrato in lista_locacoes:
        if contrato.placa_carro == placa_busca and contrato.status == 'Ativa':
            contrato_atual = contrato
            break

    if contrato_atual is None:
        print('Nenhum contrato ativo encontrado para esta placa.')
        input('Pressione Enter para retornar...')
        return

    # Data/hora da devolução (pode ser agora ou permitir que o usuário informe)
    usar_data_hora_atual = input('Usar data/hora atual para a devolução? [S/N]: ').strip().upper()[0]
    if usar_data_hora_atual == 'S':
        data_devolucao_real = datetime.now()
    else:
        # Permite que o usuário digite a data/hora da devolução (formato: DD/MM/AAAA HH:MM)
        while True:
            try:
                data_str = input('Digite a data e hora da devolução (DD/MM/AAAA HH:MM): ')
                data_devolucao_real = datetime.strptime(data_str, '%d/%m/%Y %H:%M')
                break
            except ValueError:
                print('Formato inválido. Use DD/MM/AAAA HH:MM (ex: 25/12/2025 18:30).')

    # Cálculo do atraso em horas
    if data_devolucao_real > contrato_atual.data_devolucao_prevista:
        diferenca = data_devolucao_real - contrato_atual.data_devolucao_prevista
        horas_atraso = diferenca.total_seconds() / 3600  # converte segundos para horas
        horas_atraso = round(horas_atraso, 2)           # arredonda para 2 casas
        print(f'Atraso detectado: {horas_atraso:.2f} horas.')
    else:
        horas_atraso = 0
        print('Veículo devolvido no prazo.')

    # Demais verificações (tanque, km, avarias)
    tanque_cheio = input('O tanque está cheio? [S/N]: ').strip().upper()[0]
    taxas_adicionais = 0
    if tanque_cheio == 'N':
        taxas_adicionais += 150.00

    # Quilometragem (com validação)
    while True:
        try:
            km_devolucao = float(input('Quilometragem atual (ex: 1234.56): '))
            break
        except ValueError:
            print('Valor inválido.')

    km_rodados = km_devolucao - contrato_atual.km_inicial
    if km_rodados > contrato_atual.limite_km:
        km_excedente = km_rodados - contrato_atual.limite_km
        taxas_adicionais += calcular_multa_km(km_excedente)

    possui_avarias = input('Há avarias? [S/N]: ').strip().upper()[0]
    if possui_avarias == 'S':
        while True:
            try:
                valor_avarias = float(input('Custo das avarias: R$ '))
                break
            except ValueError:
                print('Valor inválido.')
        taxas_adicionais += valor_avarias

    # Aplicar multa por atraso (se houver)
    if horas_atraso > 0:
        taxas_adicionais += calcular_multa_atraso(horas_atraso)

    valor_final = contrato_atual.valor_provisorio + taxas_adicionais

    # Exibir extrato
    print('-' * 50)
    print('EXTRATO DE DEVOLUÇÃO'.center(50))
    print('-' * 50)
    print(f'{"Placa:":<30}{contrato_atual.placa_carro:>20}')
    print(f'{"Data prevista:":<30}{contrato_atual.data_devolucao_prevista.strftime("%d/%m/%Y %H:%M"):>20}')
    print(f'{"Data devolução:":<30}{data_devolucao_real.strftime("%d/%m/%Y %H:%M"):>20}')
    if horas_atraso > 0:
        print(f'{"Horas de atraso:":<30}{f"{horas_atraso:.2f}h":>20}')  # ajuste de formatação
    print(f'{"Valor provisório:":<30}{formatar_moeda(contrato_atual.valor_provisorio):>20}')
    print(f'{"Taxas adicionais:":<30}{formatar_moeda(taxas_adicionais):>20}')
    print(f'{"Valor final:":<30}{formatar_moeda(valor_final):>20}')
    print('-' * 50)

    confirm_pag = input('Confirma o pagamento? [S/N] ').strip().upper()[0]

    if confirm_pag == 'S':
        contrato_atual.status = 'Finalizado'
        for carro in estoque_carros:
            if carro.placa == contrato_atual.placa_carro:
                carro.disponivel = True
                break
        # Salva alterações
        banco_dados.salvar_locacoes(lista_locacoes)
        banco_dados.salvar_carros(estoque_carros)
        print('Pagamento confirmado e devolução efetuada com sucesso! Veículo liberado em estoque.')
    else:
        print('Operação suspensa; o veículo permanecerá bloqueado até a confirmação do pagamento.')

    input('Pressione Enter para voltar ao menu anterior... ')
