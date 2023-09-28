class Fila:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def tamanho(self):
        return len(self.items)

    def frente(self):
        if not self.esta_vazia():
            return self.items[0]
        else:
            raise IndexError("A fila está vazia")
        
    def limpar(self):
        self.items = []

    # Verificar se um item está na fila
    def contem(self, item):
        return item in self.items
    
    def copiar(self):
        nova_fila = Fila()
        nova_fila.items = self.items.copy()
        return nova_fila

    # Converter a Fila em uma lista
    def para_lista(self):
        return self.items.copy()
    
    def inverter(self):
        self.items.reverse()

    def __str__(self):
        return str(self.items)
    
    def remover_na_posicao(self, posicao):
        if 0 <= posicao < len(self.items):
            item_removido = self.items.pop(posicao)
            return item_removido
        else:
            raise IndexError("Posição fora dos limites da fila")

    def contar_ocorrencias(self, item):
        return self.items.count(item)

    def concatenar(self, outra_fila):
        if isinstance(outra_fila, Fila):
            self.items.extend(outra_fila.items)
        else:
            raise TypeError("O objeto fornecido não é uma instância de Fila")

# Exemplo de uso:
# Criando uma fila
fila = Fila()

# Adicionando elementos à fila
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

# Tamanho da fila (deve ser 3)
print(f"Tamanho da fila: {fila.tamanho()}")

# Frente da fila (deve ser 1)
print(f"Frente da fila: {fila.frente()}")

# Removendo um item da fila (o item 1 deve ser removido)
item_removido = fila.desenfileirar()
print(f"Item removido: {item_removido}")

# Tamanho da fila após a remoção (deve ser 2)
print(f"Tamanho da fila após a remoção: {fila.tamanho()}")

# Limpando a fila
fila.limpar()
print(f"A fila está vazia após a limpeza: {fila.esta_vazia()}")

# Adicionando elementos novamente
fila.enfileirar(4)
fila.enfileirar(5)

# Verificando se a fila contém o número 4 (deve ser True)
print(f"Contém o número 4 na fila: {fila.contem(4)}")

# Criando uma cópia da fila
copia_fila = fila.copiar()

# Convertendo a cópia da fila em uma lista
copia_lista = copia_fila.para_lista()
print(f"Cópia da fila (como lista): {copia_lista}")

# Invertendo a fila
fila.inverter()
print(f"Fila invertida: {fila.para_lista()}")

# Removendo o elemento na posição 1 (o elemento 4 deve ser removido)
item_removido_na_posicao = fila.remover_na_posicao(1)
print(f"Item removido na posição 1: {item_removido_na_posicao}")

# Contando o número de ocorrências do item 4 (deve ser 0, pois ele foi removido)
ocorrencias_4 = fila.contar_ocorrencias(4)
print(f"Ocorrências do número 4 na fila: {ocorrencias_4}")

# Criando uma segunda fila
outra_fila = Fila()
outra_fila.enfileirar(6)
outra_fila.enfileirar(7)

# Concatenando as duas filas
fila.concatenar(outra_fila)

# Exibindo a fila após a concatenação
print(f"Fila após concatenação: {fila.para_lista()}")
