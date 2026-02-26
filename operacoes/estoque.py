from operacoes.cadastro import estoque_carros
from utilidades.interface import cabecalho

def estoque():
    cabecalho('ESTOQUE DE VEÍCULOS')
    if not estoque_carros:
        print('Nenhum veículo cadastrado no momento.')
    else:
        for veiculo in estoque_carros:
            if veiculo.disponivel == True:
                texto_status = 'Disponível'
            else:
                texto_status = 'Alugado'
            
            print(f'[{veiculo.placa}] {veiculo.marca} {veiculo.modelo} - Diária: R$ {veiculo.preco_diaria} ({texto_status})')

    print()
    input('Pressione Enter para voltar... ')
    