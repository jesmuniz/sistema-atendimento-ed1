class Cliente:

    def __init__(self, id, nome, telefone, prioridade=False):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.prioridade = prioridade

    def __str__(self):

        if self.prioridade:
            prioridade_texto = "Sim"
        else:
            prioridade_texto = "Não"

        return (
            f"ID: {self.id} | "
            f"Nome: {self.nome} | "
            f"Telefone: {self.telefone} | "
            f"Prioridade: {prioridade_texto}"
        )

    def to_dict(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "prioridade": self.prioridade
        }