from models.atendente import Atendente
from models.cliente import Cliente
from services.validacoes import validar_cliente, validar_atendente

clientes = []
atendentes = []


def cadastrar_cliente():

    print("\n=== Cadastro de Cliente ===")

    try:
        id_cliente = int(input("ID: "))
    except ValueError:
        print("Erro: o ID deve ser um número.")
        return

    nome_cliente = input("Nome do cliente: ")
    telefone_cliente = input("Telefone: ")

    prioridade_cliente = input(
        "Prioridade (sim/não): "
    ).strip().lower()

    prioridade = prioridade_cliente == "sim"

    if not validar_cliente(
        id_cliente,
        nome_cliente,
        telefone_cliente,
        clientes
    ):
        return

    cliente = Cliente(
        id_cliente,
        nome_cliente,
        telefone_cliente,
        prioridade
    )

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")


def buscar_cliente_por_id(id_cliente):

    for cliente in clientes:

        if cliente.id == id_cliente:

            print("Cliente encontrado:")
            print(cliente)

            return cliente

    print("Cliente não encontrado.")
    return None


def listar_clientes():

    print("\n=== Lista de Clientes ===")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(cliente)


def cadastrar_atendente():

    print("\n=== Cadastro de Atendente ===")

    try:
        id_atendente = int(input("ID: "))
    except ValueError:
        print("Erro: o ID deve ser um número.")
        return

    nome_atendente = input("Nome do atendente: ")

    if not validar_atendente(
        id_atendente,
        nome_atendente,
        atendentes
    ):
        return

    atendente = Atendente(
        id_atendente,
        nome_atendente
    )

    atendentes.append(atendente)

    print("Atendente cadastrado com sucesso!")


def buscar_atendente_por_id(id_atendente):

    for atendente in atendentes:

        if atendente.id == id_atendente:

            print("Atendente encontrado:")
            print(atendente)

            return atendente

    print("Atendente não encontrado.")
    return None


def listar_atendentes():

    print("\n=== Lista de Atendentes ===")

    if len(atendentes) == 0:
        print("Nenhum atendente cadastrado.")
        return

    for atendente in atendentes:
        print(atendente)