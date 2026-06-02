class Atendente:
    
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome}"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }