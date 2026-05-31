from models.cliente import Cliente
from models.atendente import Atendente

def validar_cliente(id_cliente, nome_cliente, telefone_cliente,clientes):
    for cliente in clientes:
        if cliente.id == id_cliente:
            print("ID já cadastrado. Tente novamente.")
            return False
        
    if nome_cliente.strip() == "":
        print("Nome não pode ser vazio. Tente novamente.")
        return False

    if telefone_cliente.strip() == "":
        print("Telefone não pode ser vazio. Tente novamente.")
        return False

    return True

def validar_atendente(id_atendente, nome_atendente, atendentes):
    for atendente in atendentes:
        if atendente.id == id_atendente:
            print("ID já cadastrado. Tente novamente.")
            return False
        
    if nome_atendente.strip() == "":
        print("Nome não pode ser vazio. Tente novamente.")
        return False
    return True

def validar_atendimento(cliente, atendente):
    if cliente is None:
        print("Cliente não encontrado. Tente novamente.")
        return False

    if atendente is None:
        print("Atendente não encontrado. Tente novamente.")
        return False

    return True