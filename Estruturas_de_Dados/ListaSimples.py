class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

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
        novo_no = No(dado)
        if self.estaVazia():
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def exibir(self):
        if self.estaVazia():
            print("A lista está vazia.")
            return
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("Nenhum")

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.dado == valor:
                return True
            atual = atual.proximo
        return False

    def remover(self, valor):
        if self.estaVazia():
            return
        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
            return
        atual = self.cabeca
        while atual.proximo:
            if atual.proximo.dado == valor:
                atual.proximo = atual.proximo.proximo
                return
            atual = atual.proximo

    def ordenar(self):
        if self.estaVazia():
            return

        # Cria uma lista para armazenar os dados da lista ligada
        dados = []

        # Percorre a lista e adiciona os dados à lista auxiliar
        atual = self.cabeca
        while atual:
            dados.append(atual.dado)
            atual = atual.proximo

        # Ordena a lista auxiliar
        dados.sort()

        # Reconstroi a lista ligada com os dados ordenados
        atual = self.cabeca
        for valor in dados:
            atual.dado = valor
            atual = atual.proximo

    def inserirPrimeiro(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserirUltimo(self, dado):
        self.adicionar(dado)

    def inserirMeio(self, dado, posicao):
        novo_no = No(dado)
        if posicao == 0:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            return
        atual = self.cabeca
        pos = 0
        while atual and pos < posicao - 1:
            atual = atual.proximo
            pos += 1
        if not atual:
            return
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

    def removerPrimeiro(self):
        if not self.estaVazia():
            self.cabeca = self.cabeca.proximo

    def removerUltimo(self):
        if self.estaVazia():
            return
        if not self.cabeca.proximo:
            self.cabeca = None
            return
        atual = self.cabeca
        while atual.proximo.proximo:
            atual = atual.proximo
        atual.proximo = None

# Exemplo de uso:
lista_ligada = ListaLigada()
lista_ligada.adicionar(1)
lista_ligada.adicionar(2)
lista_ligada.adicionar(3)

print("Tamanho da lista:", lista_ligada.tamanho())
lista_ligada.exibir()

valor_busca = 2
if lista_ligada.buscar(valor_busca):
    print(f"O valor {valor_busca} foi encontrado na lista.")
else:
    print(f"O valor {valor_busca} não foi encontrado na lista.")

valor_remocao = 2
lista_ligada.remover(valor_remocao)
lista_ligada.exibir()

print("\nInserindo no início:")
lista_ligada.inserirPrimeiro(0)
lista_ligada.exibir()

print("\nInserindo no final:")
lista_ligada.inserirUltimo(4)
lista_ligada.exibir()

print("\nInserindo no meio (posição 2):")
lista_ligada.inserirMeio(5, 2)
lista_ligada.exibir()

print("\nRemovendo primeiro elemento:")
lista_ligada.removerPrimeiro()
lista_ligada.exibir()

print("\nRemovendo último elemento:")
lista_ligada.removerUltimo()
lista_ligada.exibir()
