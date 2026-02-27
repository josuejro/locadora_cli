from utilidades import interface
import operacoes

while True:
    opc = interface.menu()

    if opc == 1:
        operacoes.cadastro.cadastrar_carro()
    elif opc == 2:
        operacoes.estoque.estoque()
    elif opc == 3:
        operacoes.cadastro.cadastrar_clientes()
    elif opc == 4:
        operacoes.locacao.realizar_locacao()
    else: 
        input('Opção inválida, pressione Enter e tente novamente.')
        break

