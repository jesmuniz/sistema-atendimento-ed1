from utils.arquivo import carregar_json, salvar_json
from models.atendente import Atendente
from models.cliente import Cliente
from services.validacoes import validar_cliente, validar_atendente
from structures.lista_encadeada import ListaEncadeada

lista_clientes_ativos = ListaEncadeada()

dados_clientes = carregar_json("data/clientes.json")
dados_atendentes = carregar_json("data/atendentes.json")

clientes = [
    Cliente(
        cliente["id"],
        cliente["nome"],
        cliente["telefone"],
        cliente["prioridade"]
    )
    for cliente in dados_clientes
]

for cliente in clientes:
    lista_clientes_ativos.inserir(cliente)

atendentes = [
    Atendente(
        atendente["id"],
        atendente["nome"]
    )
    for atendente in dados_atendentes
]


def salvar_clientes():

    salvar_json(
        "data/clientes.json",
        [cliente.to_dict() for cliente in clientes]
    )


def salvar_atendentes():

    salvar_json(
        "data/atendentes.json",
        [atendente.to_dict() for atendente in atendentes]
    )


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

    lista_clientes_ativos.inserir(cliente)

    salvar_clientes()



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

    salvar_atendentes()

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

def busca_binaria_cliente(id_cliente):

    clientes_ordenados = sorted(
        clientes,
        key=lambda cliente: cliente.id
    )

    esquerda = 0
    direita = len(clientes_ordenados) - 1

    while esquerda <= direita:

        meio = (esquerda + direita) // 2

        if clientes_ordenados[meio].id == id_cliente:
            return clientes_ordenados[meio]

        elif clientes_ordenados[meio].id < id_cliente:
            esquerda = meio + 1

        else:
            direita = meio - 1

    return None

def buscar_cliente_binaria():

    print("\n=== Busca Binária de Cliente ===")

    try:
        id_cliente = int(input("Digite o ID: "))

    except ValueError:
        print("ID inválido.")
        return

    cliente = busca_binaria_cliente(id_cliente)

    if cliente:

        print("\nCliente encontrado:")
        print(cliente)

    else:

        print("Cliente não encontrado.")

def remover_cliente_inativo():

    print("\n=== Remover Cliente Inativo ===")

    try:
        id_cliente = int(input("ID do cliente: "))

    except ValueError:
        print("ID inválido.")
        return

    cliente_encontrado = None

    for cliente in clientes:

        if cliente.id == id_cliente:

            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:

        print("Cliente não encontrado.")
        return

    clientes.remove(cliente_encontrado)

    lista_clientes_ativos.remover(id_cliente)

    salvar_clientes()

    print("Cliente removido com sucesso!")


def listar_clientes_ativos():

    print("\n=== Clientes Ativos (Lista Encadeada) ===")

    lista_clientes_ativos.listar()