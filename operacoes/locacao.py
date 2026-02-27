from operacoes.cadastro import estoque_carros
from operacoes.cadastro import lista_clientes
from modelos.contrato import Contrato
from utilidades.interface import cabecalho
from utilidades.calculos import formatar_moeda
from utilidades import banco_dados

lista_locacoes = []

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
    
    quantidade_dias = int(input('Quantidade de dias que o veículo estará alugado: '))
    quilometragem_painel = float(input('Quilometragem presente no painel do veículo: '))

    valor_total_previsto = quantidade_dias * carro_escolhido.preco_diaria

    print('-' * 50)
    print('RESUMO DA LOCAÇÃO'.center(50))
    print('-' * 50)
        
    nome_veiculo = f"{carro_escolhido.marca} {carro_escolhido.modelo}"
    texto_dias = f"{quantidade_dias} dias"
        
    print(f'{"Locador:":<30}{cliente_atual.nome:>20}')
    print(f'{"Veículo:":<30}{nome_veiculo:>20}')
    print(f'{"Dias contratados:":<30}{texto_dias:>20}')
    print(f'{"Valor provisório:":<30}{formatar_moeda(valor_total_previsto):>20}')
    print('-' * 50)
    print()

    confirm = input('Confirma a locação? [S/N]: ').strip().upper()[0]

    if confirm == 'S':
        novo_id = len(lista_locacoes) + 1

        novo_contrato = Contrato(
            id_contrato=novo_id,
            cpf_cliente=cliente_atual.cpf,
            placa_carro=carro_escolhido.placa,
            data_retirada='Imediata',               # Preenchendo buraco
            data_devolucao_prevista=quantidade_dias,
            km_inicial=quilometragem_painel,
            limite_km=1000,                         # Preenchendo buraco
            valor_provisorio=valor_total_previsto,
            seguro_e_extras='Básico',               # Preenchendo buraco
            status='Ativa'                          # Muito importante para a devolução
        )
        lista_locacoes.append(novo_contrato)
        banco_dados.salvar_locacoes(lista_locacoes)
        banco_dados.salvar_carros(estoque_carros)

        carro_escolhido.disponivel = False

        print('Locação efetuada com sucesso! Contrato gerado.')
    else:
        print('Operação cancelada.')

    input('Pressione Enter para voltar para o menu principal... ')