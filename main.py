from services.cliente_services import (
    cadastrar_cliente,
    listar_clientes,
    cadastrar_atendente,
    listar_atendentes
)

from services.atendimento_services import (
    abrir_atendimento,
    finalizar_atendimento,
    listar_historico,
    desfazer_ultima_finalizacao
)

from services.relatorio_service import (
    mostrar_relatorio,
    exportar_csv
)

from utils.logger import registrar_log


def menu():

    registrar_log("Sistema iniciado")

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
        print("8 - Desfazer Última Finalização")
        print("9 - Relatório")
        print("10 - Exportar CSV")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            cadastrar_cliente()
            registrar_log("Cadastro de cliente realizado")

        elif opcao == "2":

            cadastrar_atendente()
            registrar_log("Cadastro de atendente realizado")

        elif opcao == "3":

            listar_clientes()
            registrar_log("Listagem de clientes")

        elif opcao == "4":

            listar_atendentes()
            registrar_log("Listagem de atendentes")

        elif opcao == "5":

            abrir_atendimento()
            registrar_log("Atendimento aberto")

        elif opcao == "6":

            finalizar_atendimento()
            registrar_log("Atendimento finalizado")

        elif opcao == "7":

            listar_historico()
            registrar_log("Histórico consultado")
        
        elif opcao == "8":

             desfazer_ultima_finalizacao()

        elif opcao == "9":

             mostrar_relatorio()

        elif opcao == "10":

             exportar_csv()

        elif opcao == "0":

            registrar_log("Sistema encerrado")
            print("\nSistema encerrado.")
            break

        else:

            print("\nOpção inválida!")
            registrar_log("Tentativa de acesso com opção inválida")


if __name__ == "__main__":
    menu()