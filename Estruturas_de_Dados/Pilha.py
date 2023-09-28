class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            raise IndexError("A pilha está vazia")

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        else:
            raise IndexError("A pilha está vazia")

    def tamanho(self):
        return len(self.items)

    def limpar(self):
        self.items = []

    def inserir_no_fundo(self, item):
        self.items.insert(0, item)

    def copia(self):
        nova_pilha = Pilha()
        nova_pilha.items = self.items.copy()
        return nova_pilha

    def buscar(self, item):
        if item in self.items:
            return self.items.index(item)
        else:
            return -1

    def contar(self, item):
        return self.items.count(item)

    def inverter(self):
        self.items.reverse()

    def to_list(self):
        return self.items.copy()

    def clonar(self):
        nova_pilha = Pilha()
        for item in self.items:
            nova_pilha.empilhar(item)
        return nova_pilha

    def __str__(self):
        return f"Pilha: {self.items}"

# Exemplo de uso:
pilha = Pilha()

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)

print(f"Tamanho da pilha: {pilha.tamanho()}")
print(f"Topo da pilha: {pilha.topo()}")

item_desempilhado = pilha.desempilhar()
print(f"Item desempilhado: {item_desempilhado}")

print(f"Tamanho da pilha após o desempilhamento: {pilha.tamanho()}")

pilha.inserir_no_fundo(4)
print(f"Pilha após inserção no fundo: {pilha}")

copia_pilha = pilha.copia()
print(f"Cópia da pilha: {copia_pilha}")

posicao_2 = pilha.buscar(2)
print(f"Posição do item 2 na pilha: {posicao_2}")

quantidade_de_1s = pilha.contar(1)
print(f"Quantidade de 1s na pilha: {quantidade_de_1s}")

pilha.inverter()
print(f"Pilha invertida: {pilha}")
