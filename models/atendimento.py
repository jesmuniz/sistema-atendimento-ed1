class Atendimento:
    def __init__(
        self,
        cliente,
        atendente,
        data_inicio,
        data_fim,
        duracao
    ):
        self.cliente = cliente
        self.atendente = atendente
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.duracao = duracao