from datetime import datetime, timedelta
from operacoes.cadastro import estoque_carros
from operacoes.cadastro import lista_clientes
from modelos.contrato import Contrato
from utilidades.interface import cabecalho
from utilidades.calculos import formatar_moeda
from utilidades import banco_dados

lista_locacoes = []

precos_seguros = {
    'Básico': 10.00,
    'Plus': 60.00,
    'VIP': 140.00
}

def realizar_locacao():
    cabecalho('NOVA LOCAÇÃO')

    cpf_busca = input('Digite o CPF a ser buscado: ')
    cliente_encontrado = False
    cliente_atual = None

    for cliente in lista_clientes:
        if cliente.cpf == cpf_busca:
            cliente_encontrado = True
            cliente_atual = cliente
            break

    if cliente_encontrado == False:
        print('Erro: Cliente não cadastrado no sistema.')
        input('Pressione Enter para retornar ao menu principal... ')
        return
    
    print('Veículos disponíveis para locação: ')

    for carro in estoque_carros:
        if carro.disponivel == True:
            print(f'[{carro.placa}] {carro.marca} {carro.modelo} - Diária: {formatar_moeda(carro.preco_diaria)}')
    
    placa_escolhida = input('Digite a placa do carro escolhido pelo locador: ')
    carro_escolhido = None

    for carro in estoque_carros:
        if carro.placa == placa_escolhida and carro.disponivel == True:
            carro_escolhido = carro
            break
    
    if carro_escolhido == None:
        print('Erro: veículo indisponível ou placa incorreta.')
        input('Pressione Enter para retornar ao menu principal... ')
        return
    
    while True:
        try:
            quantidade_dias = int(input('Quantidade de dias que o veículo estará alugado: '))
            if quantidade_dias > 0:
                break
            else:
                print('A quantidade de dias deve ser maior que zero.')
        except ValueError:
            print('Valor inválido. Digite um número inteiro.')
    
    while True:
        try:
            quilometragem_painel = float(input('Quilometragem presente no painel do veículo (1234.56): '))
            break
        except ValueError:
            print('Valor inválido. Digite apenas valores numéricos (Use ponto para valores decimais).')

    valor_total_previsto = quantidade_dias * carro_escolhido.preco_diaria

    print('\nOpções de seguro:')
    for i, (tipo, preco) in enumerate(precos_seguros.items(), 1):
        print(f'{i}. {tipo} - {formatar_moeda(preco)}')
    while True:
        try:
            escolha_seguro = int(input('Escolha o seguro desejado (1/2/3): '))
            if 1 <= escolha_seguro <= len(precos_seguros):
                tipo_seguro = list(precos_seguros.keys())[escolha_seguro-1]
                custo_seguro = precos_seguros[tipo_seguro]
                break
            else:
                print('Opção inválida.')
        except ValueError:
            print('Digite um número.')

    valor_diarias = quantidade_dias * carro_escolhido.preco_diaria
    valor_total_previsto = valor_diarias + custo_seguro    

    data_retirada = datetime.now()
    data_devolucao_prevista = data_retirada + timedelta(days=quantidade_dias)

    print('-' * 50)
    print('RESUMO DA LOCAÇÃO'.center(50))
    print('-' * 50)
    print(f'{"Locador:":<30}{cliente_atual.nome:>20}')
    nome_veiculo = f"{carro_escolhido.marca} {carro_escolhido.modelo}"
    print(f'{"Veículo:":<30}{nome_veiculo:>20}')
    print(f'{"Data retirada:":<30}{data_retirada.strftime("%d/%m/%Y %H:%M"):>20}')
    print(f'{"Devolução prevista:":<30}{data_devolucao_prevista.strftime("%d/%m/%Y %H:%M"):>20}')
    print(f'{"Seguro:":<30}{tipo_seguro:>20}')
    print(f'{"Valor provisório:":<30}{formatar_moeda(valor_total_previsto):>20}')
    print('-' * 50)

    confirm = input('Confirma a locação? [S/N]: ').strip().upper()[0]

    if confirm == 'S':
        novo_id = len(lista_locacoes) + 1
        novo_contrato = Contrato(
            id_contrato=novo_id,
            cpf_cliente=cliente_atual.cpf,
            placa_carro=carro_escolhido.placa,
            data_retirada=data_retirada,
            data_devolucao_prevista=data_devolucao_prevista,
            km_inicial=quilometragem_painel,
            limite_km=1000,                      # mantido fixo
            valor_provisorio=valor_total_previsto,
            seguro_e_extras={'tipo': tipo_seguro, 'custo': custo_seguro},  # salva como dicionário
            status='Ativa'
        )
        lista_locacoes.append(novo_contrato)
        banco_dados.salvar_locacoes(lista_locacoes)

        carro_escolhido.disponivel = False
        banco_dados.salvar_carros(estoque_carros)

        print('Locação efetuada com sucesso! Contrato gerado.')
    else:
        print('Operação cancelada.')

    input('Pressione Enter para voltar ao menu...')