from services.cliente_services import (
    cadastrar_cliente,
    cadastrar_atendente,
    listar_clientes,
    listar_atendentes
)

from services.atendimento_services import (
    abrir_atendimento,
    finalizar_atendimento,
    listar_historico
)
from services.validacoes import (validar_cliente, validar_atendente)

def menu():

    while True:

        print("\n" + "=" * 40)
        print("SISTEMA DE ATENDIMENTO")
        print("=" * 40)

        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Atendente")
        print("3 - Listar Clientes")
        print("4 - Listar Atendentes")
        print("5 - Abrir Atendimento")
        print("6 - Finalizar Atendimento")
        print("7 - Ver Histórico")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            cadastrar_atendente()

        elif opcao == "3":
            listar_clientes()

        elif opcao == "4":
            listar_atendentes()

        elif opcao == "5":
            abrir_atendimento()

        elif opcao == "6":
            finalizar_atendimento()

        elif opcao == "7":
            listar_historico()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()