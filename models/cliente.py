class Cliente:
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.prioridade = False

    #criar dicionario para armazenar os clientes e coloca no json

    def to_dict(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "prioridade": self.prioridade}