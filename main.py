from utils.logger import registrar_log


def mostrar_menu():

    print("\n" + "-" * 35)
    print(" SISTEMA DE ATENDIMENTO ")
    print("-" * 35)

    print("1 - Cadastrar cliente")
    print("2 - Abrir atendimento")
    print("3 - Relatórios")
    print("0 - Sair")


def main():

    registrar_log("Sistema iniciado")

    while True:

        mostrar_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nCadastro de cliente")

        elif opcao == "2":
            print("\nAbrir atendimento")

        elif opcao == "3":
            print("\nRelatórios")

        elif opcao == "0":

            registrar_log("Sistema encerrado")

            print("\nSistema encerrado")
            break

        else:
            print("\nOpção inválida")


if __name__ == "__main__":
    main()