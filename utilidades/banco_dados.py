import pandas as pd
import os
from modelos.carro import Carro
from modelos.cliente import Cliente
from modelos.contrato import Contrato

def salvar_carros(lista_carros):
    if not lista_carros:
        return
    
    dados = []
    for carro in lista_carros:
        dados.append({
            'placa': carro.placa,
            'marca': carro.marca,
            'modelo': carro.modelo,
            'preco_diaria': carro.preco_diaria,
            'disponivel': carro.disponivel
        })
    
    df = pd.DataFrame(dados)
    df.to_csv('carros.csv', index=False)

def carregar_carros():
    lista_temp = []
    if not os.path.exists('carros.csv'):
        return lista_temp
    
    df = pd.read_csv('carros.csv')
    for _, linha in df.iterrows():
        novo_carro = Carro(
            str(linha['placa']),
            str(linha['marca']),
            str(linha['modelo']),
            float(linha['preco_diaria'])
        )
        novo_carro.disponivel = linha['disponivel'] == True
        lista_temp.append(novo_carro)
    
    return lista_temp

def salvar_clientes(lista_clientes):
    if not lista_clientes:
        return
    
    dados = []
    for cliente in lista_clientes:
        dados.append({
            'nome': cliente.nome,
            'data_nasc': cliente.data_nasc,
            'cpf': cliente.cpf,
            'cnh': cliente.cnh
        })
    
    df = pd.DataFrame(dados)
    df.to_csv('clientes.csv', index=False)

def carregar_clientes():
    lista_temp = []
    if not os.path.exists('clientes.csv'):
        return lista_temp
    
    df = pd.read_csv('clientes.csv')
    for index, linha in df.iterrows():
        novo_cliente = Cliente(
            str(linha['nome']),
            str(linha['data_nasc']),
            str(linha['cpf']),
            str(linha['cnh'])
        )
        lista_temp.append(novo_cliente)
    
    return lista_temp

def salvar_locacoes(lista_locacoes):
    if not lista_locacoes:
        return
    
    dados = []
    for contrato in lista_locacoes:
        dados.append({
            'id_contrato': contrato.id_contrato,
            'cpf_cliente': contrato.cpf_cliente,
            'placa_carro': contrato.placa_carro,
            'data_retirada': contrato.data_retirada,
            'data_devolucao_prevista': contrato.data_devolucao_prevista,
            'km_inicial': contrato.km_inicial,
            'limite_km': contrato.limite_km,
            'valor_provisorio': contrato.valor_provisorio,
            'seguro_e_extras': contrato.seguro_e_extras,
            'status': contrato.status
        })
    
    df = pd.DataFrame(dados)
    df.to_csv('locacoes.csv', index=False)

def carregar_locacoes():
    lista_temp = []
    if not os.path.exists('locacoes.csv'):
        return lista_temp
    
    df = pd.read_csv('locacoes.csv')
    for index, linha in df.iterrows():
        novo_contrato = Contrato(
            int(linha['id_contrato']),
            str(linha['cpf_cliente']),
            str(linha['placa_carro']),
            str(linha['data_retirada']),
            int(linha['data_devolucao_prevista']),
            float(linha['km_inicial']),
            float(linha['limite_km']),
            float(linha['valor_provisorio']),
            str(linha['seguro_e_extras']),
            str(linha['status'])
        )

        lista_temp.append(novo_contrato)
    
    return lista_temp
