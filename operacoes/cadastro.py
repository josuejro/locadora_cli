from modelos.carro import Carro
from modelos.cliente import Cliente
from modelos.contrato import Contrato
from utilidades.interface import cabecalho

estoque_carros = []
lista_clientes = []

def cadastrar_carro():
    cabecalho('CADASTRO DE VEÍCULO')

    placa_temp = input('Digite a placa do carro: ')
    marca_temp = input('Digite a marca do carro: ')
    modelo_temp = input('Digite o modelo do carro: ')
    preco_diaria_temp = float(input('Digite o valor da diária do carro: '))

    novo_carro = Carro(placa_temp, marca_temp, modelo_temp, preco_diaria_temp)
    estoque_carros.append(novo_carro)

    print('Carro cadastrado com sucesso!')
    input('Pressione Enter para voltar... ')

def cadastrar_clientes():
    cabecalho('CADASTRO DE CLIENTES')

    nome_temp = input('Nome do cliente: ')
    data_nasc_temp = input('Data de nascimento: ')
    cpf_temp = input('CPF: ')
    cnh_temp = input('CNH: ')

    novo_cliente = Cliente(nome_temp, data_nasc_temp, cpf_temp, cnh_temp)
    lista_clientes.append(novo_cliente)

    print('Cliente cadastrado com sucesso!')
    input('Pressione Enter para voltar... ')
