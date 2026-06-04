import csv
from services.atendimento_services import historico


def calcular_tempo_medio():

    if len(historico) == 0:
        return None

    total_segundos = 0

    for atendimento in historico:
        total_segundos += atendimento.duracao.total_seconds()

    return total_segundos / len(historico)


def mostrar_relatorio():

    print("\n=== RELATÓRIO DE ATENDIMENTOS ===")

    if len(historico) == 0:
        print("Nenhum atendimento finalizado.")
        return

    for atendimento in historico:

        print("-" * 40)

        print(f"Cliente: {atendimento.cliente.nome}")
        print(f"Atendente: {atendimento.atendente.nome}")
        print(f"Duração: {atendimento.duracao}")

    media = calcular_tempo_medio()

    print("\nTempo médio de atendimento:")
    print(f"{media:.2f} segundos")


def exportar_csv():

    with open(
        "relatorio_atendimentos.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow([
            "Cliente",
            "Atendente",
            "Inicio",
            "Fim",
            "Duracao"
        ])

        for atendimento in historico:

            writer.writerow([
                atendimento.cliente.nome,
                atendimento.atendente.nome,
                atendimento.data_inicio,
                atendimento.data_fim,
                atendimento.duracao
            ])

    print("Relatório exportado para relatorio_atendimentos.csv")