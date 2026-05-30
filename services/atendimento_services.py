from models.atendimento import Atendimento
from datetime import datetime
from validacoes import validar_atendimento

atendimentos = []
historico = []

def abrir_atendimento(cliente, atendente):
    atendimento = Atendimento(cliente, atendente)

    if not validar_atendimento(cliente, atendente):
        return
    
    atendimentos.append(atendimento)
    print("Atendimento aberto!")

def fechar_atendimento(atendimento):
    atendimento.data_fim = datetime.now()
    atendimento.duracao = atendimento.data_fim - atendimento.data_inicio
    print("Atendimento fechado! Duração: {}".format(atendimento.duracao))

def adcionar_historico(atendimento):
    print("\n=== Histórico de Atendimento ===")
    historico.append(atendimento)
    for atendimento in historico:
        print("Cliente: {}, Atendente: {}, Data início: {}, Data fim: {}, Duração: {}".format(
            atendimento.cliente.nome,
            atendimento.atendente.nome,
            atendimento.data_inicio,
            atendimento.data_fim,
            atendimento.duracao
        ))
    
