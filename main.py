from services.cliente_services import (
    cadastrar_cliente,
    listar_clientes,
    cadastrar_atendente,
    listar_atendentes,
    buscar_cliente_binaria,
    remover_cliente_inativo,
    listar_clientes_ativos
    
)

from services.atendimento_services import (
    abrir_atendimento,
    finalizar_atendimento,
    listar_historico,
    desfazer_ultima_finalizacao,
    chamar_proximo_atendimento
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
        print("5 - Buscar Cliente por ID")
        print("6 - Abrir Atendimento")
        print("7 - Chamar Próximo Atendimento")
        print("8 - Finalizar Atendimento")
        print("9 - Ver Histórico")
        print("10 - Desfazer Última Finalização")
        print("11 - Relatório")
        print("12 - Exportar CSV")
        print("13 - Remover Cliente Inativo")
        print("14 - Listar Clientes Ativos")
        print("0 - Sair")

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

            buscar_cliente_binaria()

        elif opcao == "6":

            abrir_atendimento()
            registrar_log("Cliente entrou na fila")

        elif opcao == "7":

            chamar_proximo_atendimento()
            registrar_log("Próximo atendimento chamado")

        elif opcao == "8":

            finalizar_atendimento()
            registrar_log("Atendimento finalizado")

        elif opcao == "9":

            listar_historico()
            registrar_log("Histórico consultado")

        elif opcao == "10":

            desfazer_ultima_finalizacao()
            registrar_log("Última finalização desfeita")

        elif opcao == "11":

            mostrar_relatorio()
            registrar_log("Relatório gerado")

        elif opcao == "12":

            exportar_csv()
            registrar_log("Relatório exportado para CSV")
        
        elif opcao == "13":

            remover_cliente_inativo()

        elif opcao == "14":

            listar_clientes_ativos()

        elif opcao == "0":

            registrar_log("Sistema encerrado")
            print("\nSistema encerrado.")
            break

        else:

            print("\nOpção inválida!")
            registrar_log("Tentativa de acesso com opção inválida")


if __name__ == "__main__":
    menu()