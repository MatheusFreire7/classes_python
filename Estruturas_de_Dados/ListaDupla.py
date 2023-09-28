class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteLigada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def estaVazia(self):
        return self.cabeca is None

    def tamanho(self):
        tamanho = 0
        atual = self.cabeca
        while atual:
            tamanho += 1
            atual = atual.proximo
        return tamanho

    def adicionar(self, dado):
        novo_no = NoDuplo(dado)
        if self.estaVazia():
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no

    def exibir_frente(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("Nenhum")

    def exibir_tras(self):
        atual = self.cauda
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.anterior
        print("Nenhum")

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.dado == valor:
                return True
            atual = atual.proximo
        return False

    def remover(self, valor):
        atual = self.cabeca
        while atual:
            if atual.dado == valor:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.cauda = atual.anterior

                return
            atual = atual.proximo

    def inserirPrimeiro(self, dado):
        novo_no = NoDuplo(dado)
        if self.estaVazia():
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no

    def inserirUltimo(self, dado):
        self.adicionar(dado)

    def inserirMeio(self, dado, posicao):
        novo_no = NoDuplo(dado)
        atual = self.cabeca
        pos = 0
        while atual:
            if pos == posicao:
                novo_no.anterior = atual.anterior
                novo_no.proximo = atual
                if atual.anterior:
                    atual.anterior.proximo = novo_no
                else:
                    self.cabeca = novo_no
                atual.anterior = novo_no
                return
            atual = atual.proximo
            pos += 1

    def removerPrimeiro(self):
        if not self.estaVazia():
            if self.cabeca == self.cauda:
                self.cabeca = None
                self.cauda = None
            else:
                self.cabeca = self.cabeca.proximo
                self.cabeca.anterior = None

    def removerUltimo(self):
        if not self.estaVazia():
            if self.cabeca == self.cauda:
                self.cabeca = None
                self.cauda = None
            else:
                self.cauda = self.cauda.anterior
                self.cauda.proximo = None

    def ordenar(self):
        if self.estaVazia():
            return

        # Cria uma lista para armazenar os dados da lista duplamente ligada
        dados = []

        # Percorre a lista e adiciona os dados à lista auxiliar
        atual = self.cabeca
        while atual:
            dados.append(atual.dado)
            atual = atual.proximo

        # Ordena a lista auxiliar
        dados.sort()

        # Reconstroi a lista duplamente ligada com os dados ordenados
        atual = self.cabeca
        for valor in dados:
            atual.dado = valor
            atual = atual.proximo

# Exemplo de uso:
lista_dupla = ListaDuplamenteLigada()
lista_dupla.adicionar(1)
lista_dupla.adicionar(2)
lista_dupla.adicionar(3)

print("Exibindo na frente:")
lista_dupla.exibir_frente()

print("\nExibindo atrás:")
lista_dupla.exibir_tras()

valor_busca = 2
if lista_dupla.buscar(valor_busca):
    print(f"O valor {valor_busca} foi encontrado na lista.")
else:
    print(f"O valor {valor_busca} não foi encontrado na lista.")

valor_remocao = 2
lista_dupla.remover(valor_remocao)

print("\nExibindo após a remoção:")
lista_dupla.exibir_frente()

print("Tamanho da lista:", lista_dupla.tamanho())
print("A lista está vazia?", lista_dupla.estaVazia())

print("\nInserindo no início:")
lista_dupla.inserirPrimeiro(0)
lista_dupla.exibir_frente()

print("\nInserindo no final:")
lista_dupla.inserirUltimo(4)
lista_dupla.exibir_frente()

print("\nInserindo no meio (posição 2):")
lista_dupla.inserirMeio(5, 2)
lista_dupla.exibir_frente()

print("\nRemovendo primeiro elemento:")
lista_dupla.removerPrimeiro()
lista_dupla.exibir_frente()

print("\nRemovendo último elemento:")
lista_dupla.removerUltimo()
lista_dupla.exibir_frente()

print("Antes de ordenar:")
lista_dupla.exibir_frente()

lista_dupla.ordenar()

print("\nDepois de ordenar:")
lista_dupla.exibir_frente()

