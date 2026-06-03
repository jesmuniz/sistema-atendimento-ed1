class No:

    def __init__(self, cliente):

        self.cliente = cliente
        self.proximo = None


class ListaEncadeada:

    def __init__(self):

        self.inicio = None

    def inserir(self, cliente):

        novo_no = No(cliente)

        if self.inicio is None:

            self.inicio = novo_no
            return

        atual = self.inicio

        while atual.proximo is not None:

            atual = atual.proximo

        atual.proximo = novo_no

    def remover(self, id_cliente):

        if self.inicio is None:
            return False

        if self.inicio.cliente.id == id_cliente:

            self.inicio = self.inicio.proximo
            return True

        atual = self.inicio

        while atual.proximo is not None:

            if atual.proximo.cliente.id == id_cliente:

                atual.proximo = atual.proximo.proximo
                return True

            atual = atual.proximo

        return False

    def listar(self):

        atual = self.inicio

        while atual is not None:

            print(atual.cliente)

            atual = atual.proximo