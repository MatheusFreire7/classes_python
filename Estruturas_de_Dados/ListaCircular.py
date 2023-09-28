class NoListaCircular:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigadaCircular:
    def __init__(self):
        self.cabeca = None

    def esta_vazia(self):
        return self.cabeca is None

    def adicionar(self, dado):
        novo_no = NoListaCircular(dado)
        if self.esta_vazia():
            self.cabeca = novo_no
            novo_no.proximo = self.cabeca
        else:
            atual = self.cabeca
            while atual.proximo != self.cabeca:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.cabeca

    def remover(self, dado):
        if not self.esta_vazia():
            if self.cabeca.dado == dado:
                if self.cabeca.proximo == self.cabeca:
                    self.cabeca = None
                else:
                    atual = self.cabeca
                    while atual.proximo != self.cabeca:
                        anterior = atual
                        atual = atual.proximo
                    anterior.proximo = self.cabeca
                    self.cabeca = self.cabeca.proximo
                return

            atual = self.cabeca
            while atual.proximo != self.cabeca:
                anterior = atual
                atual = atual.proximo
                if atual.dado == dado:
                    anterior.proximo = atual.proximo
                    return

    def exibir(self):
        if not self.esta_vazia():
            atual = self.cabeca
            while True:
                print(atual.dado, end=" -> ")
                atual = atual.proximo
                if atual == self.cabeca:
                    break
            print()

    def verificar_existencia(self, dado):
        if not self.esta_vazia():
            atual = self.cabeca
            while True:
                if atual.dado == dado:
                    return True
                atual = atual.proximo
                if atual == self.cabeca:
                    break
        return False
    
    def tamanho(self):
        count = 0
        if not self.esta_vazia():
            atual = self.cabeca
            while True:
                count += 1
                atual = atual.proximo
                if atual == self.cabeca:
                    break
        return count

    def obter_elemento(self, indice):
        if not self.esta_vazia():
            atual = self.cabeca
            for i in range(indice):
                atual = atual.proximo
            return atual.dado
        raise IndexError("Índice fora dos limites da lista")

    def inserir_elemento(self, indice, dado):
        novo_no = NoListaCircular(dado)
        if indice == 0:
            self.adicionar_no_inicio(novo_no)
        else:
            atual = self.cabeca
            for i in range(indice - 1):
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    def adicionar_no_inicio(self, novo_no):
        if self.esta_vazia():
            self.cabeca = novo_no
            novo_no.proximo = self.cabeca
        else:
            atual = self.cabeca
            while atual.proximo != self.cabeca:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no

    def remover_no_inicio(self):
        if not self.esta_vazia():
            if self.cabeca.proximo == self.cabeca:
                self.cabeca = None
            else:
                atual = self.cabeca
                while atual.proximo != self.cabeca:
                    anterior = atual
                    atual = atual.proximo
                anterior.proximo = self.cabeca
                self.cabeca = self.cabeca.proximo

    def remover_no_final(self):
        if not self.esta_vazia():
            if self.cabeca.proximo == self.cabeca:
                self.cabeca = None
            else:
                atual = self.cabeca
                while atual.proximo != self.cabeca:
                    anterior = atual
                    atual = atual.proximo
                anterior.proximo = self.cabeca

    def inverter(self):
        if not self.esta_vazia():
            prev = None
            atual = self.cabeca
            while True:
                next_node = atual.proximo
                atual.proximo = prev
                prev = atual
                atual = next_node
                if atual == self.cabeca:
                    break
            self.cabeca.proximo = prev

    def copiar(self):
        new_list = ListaLigadaCircular()
        if not self.esta_vazia():
            atual = self.cabeca
            while True:
                new_list.adicionar(atual.dado)
                atual = atual.proximo
                if atual == self.cabeca:
                    break
        return new_list

    def concatenar(self, outra_lista):
        if isinstance(outra_lista, ListaLigadaCircular):
            if not outra_lista.esta_vazia():
                atual = outra_lista.cabeca
                while True:
                    self.adicionar(atual.dado)
                    atual = atual.proximo
                    if atual == outra_lista.cabeca:
                        break

# Exemplo de uso:
# Criando uma lista circular
lista_circular = ListaLigadaCircular()

# Adicionando elementos à lista
lista_circular.adicionar(1)
lista_circular.adicionar(2)
lista_circular.adicionar(3)

# Exibindo a lista
print("Lista circular inicial:")
lista_circular.exibir()

# Verificando o tamanho da lista
print("Tamanho da lista:", lista_circular.tamanho())

# Obtendo elementos por índice
print("Elemento no índice 0:", lista_circular.obter_elemento(0))
print("Elemento no índice 1:", lista_circular.obter_elemento(1))
print("Elemento no índice 2:", lista_circular.obter_elemento(2))

# Inserindo um elemento em uma posição específica
lista_circular.inserir_elemento(1, 4)
print("Inserindo o elemento 4 no índice 1:")
lista_circular.exibir()
