
from models.atendente import Atendente
from models.cliente import Cliente
from services.validacoes import validar_cliente, validar_atendente;
clientes = []
atendentes = []

def cadastrar_cliente():
    print("\n=== Cadastro de Cliente ===")
    id_cliente = int(input("ID: "))
    nome_cliente = input("Nome cliente: ")
    telefone_cliente = input("Telefone: ")
    prioridade_cliente = input("Prioridade (sim/não): ").lower()
    if prioridade_cliente == 'sim':
        prioridade = True
    else:
        prioridade = False

    if not validar_cliente(id_cliente, nome_cliente, telefone_cliente,clientes):
        return

    cliente = Cliente(id_cliente, nome_cliente, telefone_cliente, prioridade)

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
    for cliente in clientes:
        print(cliente)

def cadastrar_atendente():
    print("\n=== Cadastro de Atendente ===")
    id_atendente = int(input("ID: "))
    nome_atendente = input("Nome atendente: ")

    if not validar_atendente(id_atendente, nome_atendente, atendentes):
        return

    atendente = Atendente(id_atendente, nome_atendente)
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
    for atendente in atendentes:
        print(atendente)


