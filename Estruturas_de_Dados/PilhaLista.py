class PilhaLista:
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

    def copiar(self):
        return self.items.copy()

    def contem(self, item):
        return item in self.items

    def inverter(self):
        self.items.reverse()

    def __str__(self):
        return str(self.items)

    def is_equal(self, outra_pilha):
        return self.items == outra_pilha

    def duplicar(self):
        self.items.extend(self.items)

    def obter_n_elementos(self, n):
        if n <= self.tamanho():
            return self.items[-n:]
        else:
            raise ValueError("Número de elementos solicitados excede o tamanho da pilha")

    def pop_todos(self):
        while not self.esta_vazia():
            self.desempilhar()

    def buscar(self, item):
        return self.items.index(item) if item in self.items else -1  # Retorna o índice do item na pilha, -1 se não encontrado

    def contar(self, item):
        return self.items.count(item)  # Conta quantas vezes um item aparece na pilha

    def inverter_copia(self):
        nova_pilha = PilhaLista()
        nova_pilha.items = self.items[::-1]
        return nova_pilha  # Retorna uma nova pilha com os elementos invertidos

    def empilhar_todos(self, lista):
        self.items.extend(lista)  # Empilha todos os elementos de uma lista na pilha

# Exemplo de uso:
pilha = PilhaLista()

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)

print(f"Tamanho da pilha: {pilha.tamanho()}")
print(f"Topo da pilha: {pilha.topo()}")

item_desempilhado = pilha.desempilhar()
print(f"Item desempilhado: {item_desempilhado}")

print(f"Tamanho da pilha após o desempilhamento: {pilha.tamanho()}")

pilha.limpar()
print(f"Pilha após a limpeza: {pilha.copiar()}")

pilha.empilhar(4)
pilha.empilhar(5)
print(f"Pilha após a empilhamento de 4 e 5: {pilha.copiar()}")

print(f"A pilha contém o número 3? {pilha.contem(3)}")
print(f"A pilha contém o número 6? {pilha.contem(4)}")