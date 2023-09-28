class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [{} for _ in range(tamanho)]

    def calcular_hash(self, chave):
        return hash(chave) % self.tamanho

    def __setitem__(self, chave, valor):
        indice = self.calcular_hash(chave)
        self.tabela[indice][chave] = valor

    def __getitem__(self, chave):
        indice = self.calcular_hash(chave)
        if chave in self.tabela[indice]:
            return self.tabela[indice][chave]
        raise KeyError(f'Chave "{chave}" não encontrada na tabela de hash.')

    def __delitem__(self, chave):
        indice = self.calcular_hash(chave)
        if chave in self.tabela[indice]:
            del self.tabela[indice][chave]
        else:
            raise KeyError(f'Chave "{chave}" não encontrada na tabela de hash.')

    def __contains__(self, chave):
        indice = self.calcular_hash(chave)
        return chave in self.tabela[indice]

    def mostrar_tabela(self):
        for i, entrada in enumerate(self.tabela):
            for chave, valor in entrada.items():
                print(f'Índice {i}: Chave="{chave}", Valor="{valor}"')

    def keys(self):
        """Retorna uma lista de todas as chaves na tabela hash."""
        keys = []
        for entrada in self.tabela:
            keys.extend(entrada.keys())
        return keys

    def values(self):
        """Retorna uma lista de todos os valores na tabela hash."""
        values = []
        for entrada in self.tabela:
            values.extend(entrada.values())
        return values

    def items(self):
        """Retorna uma lista de tuplas (chave, valor) de todos os itens na tabela hash."""
        items = []
        for entrada in self.tabela:
            items.extend(entrada.items())
        return items

    def __len__(self):
        """Retorna o número de itens na tabela hash."""
        count = 0
        for entrada in self.tabela:
            count += len(entrada)
        return count

    def clear(self):
        """Remove todos os itens da tabela hash, deixando-a vazia."""
        self.tabela = [{} for _ in range(self.tamanho)]

# Exemplo de uso:
tabela_hash = TabelaHash()

tabela_hash["chave1"] = "valor1"
tabela_hash["chave2"] = "valor2"
tabela_hash["chave3"] = "valor3"

print("Chaves:", tabela_hash.keys())
print("Valores:", tabela_hash.values())
print("Itens:", tabela_hash.items())
print("Tamanho:", len(tabela_hash))