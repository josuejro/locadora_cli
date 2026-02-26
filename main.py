from utilidades import interface

while True:
    opc = interface.menu()

    if opc == 1:
        #função futura
        interface.menu()
    else: 
        input('Opção inválida, pressione Enter e tente novamente.')
        break

