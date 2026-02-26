import os
import subprocess

def limpar_tela():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

def cabecalho(txt):
    tam = len(txt) + 4
    linha = '-' * tam

    limpar_tela()
    print(f'{linha}')
    print(f'{txt.center(tam)}')
    print(f'{linha}')
    print()

def menu():
    cabecalho('SISTEMA DE LOCADORA DE CARROS')

    print('1: Cadastrar novo carro')
    print('2: Ver estoque de carros')
    print('3: Cadastrar cliente')
    print('4: Ir para a locação')
    print('5: Ir para a devolução')
    print('6: Sair do programa')
    print()

    opc = int(input('Escolha uma opção: '))
    return opc