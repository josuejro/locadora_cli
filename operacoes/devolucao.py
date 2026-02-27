from operacoes.locacao import lista_locacoes
from operacoes.cadastro import estoque_carros
from utilidades.interface import cabecalho

def realizar_devolução():
    cabecalho('DEVOLUÇÃO DE VEÍCULO')

    placa_busca = input('Digite a placa do veículo: ')
    contrato_atual = None

    for contrato in lista_locacoes:
        if contrato.placa_carro == placa_busca and contrato.status == 'Ativa':
            contrato_atual = contrato
            break
    
    if contrato_atual is None:
        print('Nenhum contrato foi encontrado para esta placa.')
        input('Pressione Enter para retornar... ')
        return
    
    tanque_cheio = input('O tanque do carro está cheio? [S/N]: ').strip().upper()[0]
    taxas_adicionais = 0
    if tanque_cheio == 'N':
        taxas_adicionais = taxas_adicionais + 150.00

    km_devolução = float(input('Quilometragem após devolução: '))
    km_rodados = km_devolução - contrato_atual.km_inicial

    if km_rodados > contrato_atual.limite_km:
        km_excedente = km_rodados - contrato_atual.limite_km
        taxas_adicionais = taxas_adicionais + (km_excedente * 2.50)
    
    possui_avarias = input('Há avarias no veículo devolvido? [S/N]: ').strip().upper()[0]
    
    if possui_avarias == 'S':
        valor_avarias = float(input('Insira o custo das avarias identificadas: R$ '))
        taxas_adicionais = taxas_adicionais + valor_avarias
    
    horas_atraso = 0
    horas_atraso = float(input('Horas de atraso da entrega do veículo: '))

    if horas_atraso > 0:
        taxas_adicionais = taxas_adicionais + (horas_atraso * 30)
    else:
        print('Veículo entregue no horário.')
    
    valor_final = contrato_atual.valor_provisorio
    valor_final = valor_final + taxas_adicionais

    print('-------------Extrato de Devolução-------------')
    print(f'Placa do Veículo: {contrato_atual.placa_carro}')
    print(f'Valor provisório: R$ {contrato_atual.valor_provisorio:.2f}')
    print(f'Total de multas e taxas adicionais: R$ {taxas_adicionais}')
    print(f'Valor final a pagar: {valor_final:.2f}')

    confirm_pag = input('Confirma o pagamento? [S/N] ').strip().upper()[0]

    if confirm_pag == 'S':
        contrato_atual.status = 'Finalizado'

        for carro in estoque_carros:
            if carro.placa == contrato_atual.placa_carro:
                carro.disponivel = True
                break

        print('Pagamento confirmado e devolução efetuada com sucesso! Veículo liberado em estoque.')
    else:
        print('Operação suspensa; o veículo permanecerá bloqueado até a confirmação do pagamento.')

    input('Pressione Enter para voltar ao menu anterior... ')
