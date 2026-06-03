from models.atendimento import Atendimento
from datetime import datetime
from services.cliente_services import (
    buscar_cliente_por_id,
    buscar_atendente_por_id
)

atendimentos = []
historico = []
pilha_desfazer = []

fila_comum = []
fila_prioridade = []


def abrir_atendimento():

    print("\n=== Entrar na Fila ===")

    try:
        id_cliente = int(input("ID do cliente: "))

    except ValueError:
        print("Erro: digite apenas números para o ID.")
        return

    cliente = buscar_cliente_por_id(id_cliente)

    if cliente is None:
        return

    if cliente.prioridade:

        fila_prioridade.append(cliente)

        print("Cliente adicionado à fila prioritária!")

    else:

        fila_comum.append(cliente)

        print("Cliente adicionado à fila comum!")


def chamar_proximo_atendimento():

    print("\n=== Chamar Próximo Atendimento ===")

    if len(fila_prioridade) > 0:

        cliente = fila_prioridade.pop(0)

    elif len(fila_comum) > 0:

        cliente = fila_comum.pop(0)

    else:

        print("Nenhum cliente na fila.")
        return

    try:

        id_atendente = int(input("ID do atendente: "))

    except ValueError:

        print("Erro: digite apenas números para o ID.")
        return

    atendente = buscar_atendente_por_id(id_atendente)

    if atendente is None:
        return

    atendimento = Atendimento(cliente, atendente)

    atendimentos.append(atendimento)

    print(
        f"Atendimento iniciado para {cliente.nome}"
    )


def finalizar_atendimento():

    print("\n=== Finalizar Atendimento ===")

    if len(atendimentos) == 0:

        print("Não há atendimentos abertos.")
        return

    atendimento = atendimentos[-1]

    atendimento.data_fim = datetime.now()
    atendimento.duracao = (
        atendimento.data_fim -
        atendimento.data_inicio
    )

    adicionar_historico(atendimento)

    pilha_desfazer.append(atendimento)

    atendimentos.remove(atendimento)

    print("Atendimento finalizado com sucesso!")
    print(f"Duração: {atendimento.duracao}")


def adicionar_historico(atendimento):

    historico.append(atendimento)


def listar_historico():

    print("\n=== Histórico de Atendimento ===")

    if len(historico) == 0:

        print("Nenhum atendimento finalizado.")
        return

    for atendimento in historico:

        print("-" * 40)

        print(f"Cliente: {atendimento.cliente.nome}")
        print(f"Atendente: {atendimento.atendente.nome}")
        print(f"Início: {atendimento.data_inicio}")
        print(f"Fim: {atendimento.data_fim}")
        print(f"Duração: {atendimento.duracao}")


def desfazer_ultima_finalizacao():

    print("\n=== Desfazer Última Finalização ===")

    if len(pilha_desfazer) == 0:

        print("Nenhuma finalização para desfazer.")
        return

    atendimento = pilha_desfazer.pop()

    historico.remove(atendimento)

    atendimento.data_fim = None
    atendimento.duracao = None

    atendimentos.append(atendimento)

    print("Última finalização desfeita com sucesso!")