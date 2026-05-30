import csv


def exportar_csv(atendimentos):

    with open(
        "relatorio.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow([
            "Cliente",
            "Atendente",
            "Duração"
        ])

        for atendimento in atendimentos:

            writer.writerow([
                atendimento["cliente"],
                atendimento["atendente"],
                atendimento["duracao"]
            ])