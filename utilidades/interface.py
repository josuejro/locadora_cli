import subprocess
import sys

def limpar_tela():
    if sys.platform == "win32":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"])

def cabecalho(txt):
    tam = 50
    linha = "-" * tam

    limpar_tela()
    print(linha)
    print(txt.center(tam))
    print(linha)
    print()

def menu():
    while True:
        cabecalho("SISTEMA DE LOCADORA DE CARROS")

        print("1: Cadastrar novo carro")
        print("2: Ver estoque de carros")
        print("3: Cadastrar cliente")
        print("4: Ir para a locação")
        print("5: Ir para a devolução")
        print("6: Sair do programa")
        print()

        entrada = input("Escolha uma opção: ").strip()
        try:
            opc = int(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número.")
            input("Pressione Enter para continuar... ")
            continue

        if 1 <= opc <= 6:
            return opc

        print("Opção inválida. Digite o número de uma opção válida.")
        input("Pressione Enter para continuar... ")