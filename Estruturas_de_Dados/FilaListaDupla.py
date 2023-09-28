class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class FilaListaDuplamenteLigada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def esta_vazia(self):
        return self.cabeca is None

    def enfileirar(self, dado):
        novo_no = NoDuplo(dado)
        if self.cauda is None:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        dado = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        if self.cabeca is None:
            self.cauda = None
        else:
            self.cabeca.anterior = None
        return dado

    def tamanho(self):
        tamanho = 0
        atual = self.cabeca
        while atual:
            tamanho += 1
            atual = atual.proximo
        return tamanho
    
    def primeiro(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        return self.cabeca.dado

    def ultimo(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        return self.cauda.dado

    def contem(self, dado):
        atual = self.cabeca
        while atual:
            if atual.dado == dado:
                return True
            atual = atual.proximo
        return False

    def esvaziar(self):
        self.cabeca = None
        self.cauda = None

    def copiar(self):
        nova_fila = FilaListaDuplamenteLigada()
        atual = self.cabeca
        while atual:
            nova_fila.enfileirar(atual.dado)
            atual = atual.proximo
        return nova_fila

    def to_list(self):
        lista = []
        atual = self.cabeca
        while atual:
            lista.append(atual.dado)
            atual = atual.proximo
        return lista

    def inverter(self):
        atual = self.cabeca
        while atual:
            atual.anterior, atual.proximo = atual.proximo, atual.anterior
            atual = atual.anterior
        self.cabeca, self.cauda = self.cauda, self.cabeca

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return repr(self.to_list())

# Exemplo de uso:
fila = FilaListaDuplamenteLigada()

fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print(f"Tamanho da fila: {fila.tamanho()}")

item_removido = fila.desenfileirar()
print(f"Item removido: {item_removido}")

print(f"Tamanho da fila após a remoção: {fila.tamanho()}")

print(f"Tamanho da fila: {fila.tamanho()}")
print(f"Primeiro item da fila: {fila.primeiro()}")
print(f"Último item da fila: {fila.ultimo()}")
print(f"A fila contém o número 2? {fila.contem(2)}")

fila2 = fila.copiar()
print(f"Cópia da fila: {fila2}")

fila.inverter()
print(f"Fila invertida: {fila.to_list()}")

print(f"String representando a fila: {str(fila)}")
