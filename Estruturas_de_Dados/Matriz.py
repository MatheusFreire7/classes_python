import numpy as np

class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.dados = [[0 for _ in range(colunas)] for _ in range(linhas)]

    def definir_valor(self, linha, coluna, valor):
        if 1 <= linha <= self.linhas and 1 <= coluna <= self.colunas:
            self.dados[linha - 1][coluna - 1] = valor
        else:
            raise IndexError("Índices fora dos limites da matriz")

    def obter_valor(self, linha, coluna):
        if 1 <= linha <= self.linhas and 1 <= coluna <= self.colunas:
            return self.dados[linha - 1][coluna - 1]
        else:
            raise IndexError("Índices fora dos limites da matriz")

    def mostrar_matriz(self):
        for linha in self.dados:
            for elemento in linha:
                print(elemento, end=" ")
            print()

    @property
    def numero_linhas(self):
        return self.linhas

    @property
    def numero_colunas(self):
        return self.colunas

    def __str__(self):
        matriz_str = ""
        for linha in self.dados:
            matriz_str += " ".join(map(str, linha)) + "\n"
        return matriz_str.strip()

    def matriz_transposta(self):
        transposta = [[self.dados[j][i] for j in range(self.linhas)] for i in range(self.colunas)]
        return Matriz(self.colunas, self.linhas).criar_a_partir_de_lista(transposta)

    def somar_matriz(self, outra_matriz):
        if self.linhas == outra_matriz.numero_linhas and self.colunas == outra_matriz.numero_colunas:
            resultado = [[self.dados[i][j] + outra_matriz.obter_valor(i + 1, j + 1) for j in range(self.colunas)] for i in range(self.linhas)]
            return Matriz(self.linhas, self.colunas).criar_a_partir_de_lista(resultado)
        else:
            raise ValueError("As matrizes têm tamanhos diferentes e não podem ser somadas.")

    def multiplicar_por_escalar(self, escalar):
        resultado = [[self.dados[i][j] * escalar for j in range(self.colunas)] for i in range(self.linhas)]
        return Matriz(self.linhas, self.colunas).criar_a_partir_de_lista(resultado)

    def multiplicar_matriz(self, outra_matriz):
        if self.colunas == outra_matriz.numero_linhas:
            resultado = [[sum(self.dados[i][k] * outra_matriz.obter_valor(k + 1, j + 1) for k in range(self.colunas)) for j in range(outra_matriz.numero_colunas)] for i in range(self.linhas)]
            return Matriz(self.linhas, outra_matriz.numero_colunas).criar_a_partir_de_lista(resultado)
        else:
            raise ValueError("As dimensões das matrizes não são compatíveis para multiplicação.")

    def criar_a_partir_de_lista(self, lista):
        matriz = Matriz(len(lista), len(lista[0]))
        for i in range(matriz.linhas):
            for j in range(matriz.colunas):
                matriz.dados[i][j] = lista[i][j]
        return matriz

    
    def verificar_simetrica(self):
        if self.linhas != self.colunas:
            return False

        for i in range(self.linhas):
            for j in range(i + 1, self.colunas):
                if self.dados[i][j] != self.dados[j][i]:
                    return False
        return True

    def verificar_identidade(self):
        if self.linhas != self.colunas:
            return False

        for i in range(self.linhas):
            for j in range(self.colunas):
                if i == j and self.dados[i][j] != 1:
                    return False
                elif i != j and self.dados[i][j] != 0:
                    return False
        return True

    def copiar(self):
        return Matriz(self.linhas, self.colunas).criar_a_partir_de_lista(self.dados)

    def zerar(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.dados[i][j] = 0

    def preencher(self, valor):
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.dados[i][j] = valor

    def igual(self, outra_matriz):
        if self.linhas != outra_matriz.numero_linhas or self.colunas != outra_matriz.numero_colunas:
            return False

        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.dados[i][j] != outra_matriz.obter_valor(i + 1, j + 1):
                    return False
        return True
    
    def matriz_nula(self):
        return all(all(elemento == 0 for elemento in linha) for linha in self.dados)

    def matriz_diagonal(self):
        if self.linhas != self.colunas:
            return False
        return all(self.dados[i][j] == 0 for i in range(self.linhas) for j in range(self.colunas) if i != j)

    def matriz_escalar(self):
        if self.linhas != self.colunas:
            return False
        primeiro_elemento = self.dados[0][0]
        return all(self.dados[i][j] == primeiro_elemento for i in range(self.linhas) for j in range(self.colunas))

    def matriz_triangular_superior(self):
        if self.linhas != self.colunas:
            return False
        return all(self.dados[i][j] == 0 for i in range(self.linhas) for j in range(i))

    def matriz_triangular_inferior(self):
        if self.linhas != self.colunas:
            return False
        return all(self.dados[i][j] == 0 for i in range(self.linhas) for j in range(i + 1, self.colunas))

    def inverter_sinal(self):
        return Matriz(self.linhas, self.colunas, [[-elemento for elemento in linha] for linha in self.dados])
    
    def determinante(self):
        if self.linhas != self.colunas:
            raise ValueError("A matriz deve ser quadrada para calcular o determinante.")
        if self.linhas == 1:
            return self.dados[0][0]
        if self.linhas == 2:
            return (self.dados[0][0] * self.dados[1][1]) - (self.dados[0][1] * self.dados[1][0])
        det = 0
        for coluna in range(self.colunas):
            cofator = self.cofator(0, coluna)
            det += self.dados[0][coluna] * cofator
        return det

    def cofator(self, linha, coluna):
        menor_matriz = [[self.dados[i][j] for j in range(self.colunas) if j != coluna] for i in range(self.linhas) if i != linha]
        cofator = Matriz(len(menor_matriz), len(menor_matriz[0]))
        cofator = cofator.criar_a_partir_de_lista(menor_matriz)
        return (-1) ** (linha + coluna) * cofator.determinante()
    
    def sistema_linear(self):
        if self.linhas < self.colunas - 1:
            raise ValueError("A matriz não pode ser convertida em um sistema linear completo.")
        elif self.linhas == self.colunas - 1:
            coeficientes = [[self.dados[i][j] for j in range(self.colunas - 1)] for i in range(self.linhas)]
            resultados = [self.dados[i][self.colunas - 1] for i in range(self.linhas)]
            solucao = np.linalg.solve(coeficientes, resultados)
            return solucao
        else:
            return None  # A matriz não forma um sistema linear completo


    def classificar_sistema_linear(self):
        if self.linhas < self.colunas - 1:
            return "Impossível"
        elif self.linhas == self.colunas - 1:
            return "Possível e determinado"
        else:
            augmented_matrix = np.array(self.dados)
            coefficients = augmented_matrix[:, :-1]
            constants = augmented_matrix[:, -1]

            if np.linalg.matrix_rank(coefficients) == np.linalg.matrix_rank(augmented_matrix):
                return "Possível e indeterminado"
            else:
                return "Impossível"

# Exemplo de uso:
# Criando matrizes para testes
matriz1 = Matriz(2, 3)
matriz1.definir_valor(1, 1, 1)
matriz1.definir_valor(1, 2, 2)
matriz1.definir_valor(1, 3, 3)
matriz1.definir_valor(2, 1, 4)
matriz1.definir_valor(2, 2, 5)
matriz1.definir_valor(2, 3, 6)

matriz2 = Matriz(2, 3)
matriz2.definir_valor(1, 1, 2)
matriz2.definir_valor(1, 2, 4)
matriz2.definir_valor(1, 3, 6)
matriz2.definir_valor(2, 1, 8)
matriz2.definir_valor(2, 2, 10)
matriz2.definir_valor(2, 3, 12)

# Teste de matriz transposta
print("Matriz 1:")
print(matriz1)
print("Matriz transposta de matriz 1:")
print(matriz1.matriz_transposta())

# Teste de soma de matrizes
print("Matriz 1:")
print(matriz1)
print("Matriz 2:")
print(matriz2)
soma_matrizes = matriz1.somar_matriz(matriz2)
print("Soma das matrizes 1 e 2:")
print(soma_matrizes)

# Teste de multiplicação por escalar
print("Matriz 1:")
print(matriz1)
escalar = 2
resultado_multiplicacao = matriz1.multiplicar_por_escalar(escalar)
print(f"Matriz 1 multiplicada por {escalar}:")
print(resultado_multiplicacao)

# Teste de multiplicação de matrizes
matriz3 = Matriz(3, 2)
matriz3.definir_valor(1, 1, 1)
matriz3.definir_valor(1, 2, 2)
matriz3.definir_valor(2, 1, 3)
matriz3.definir_valor(2, 2, 4)
matriz3.definir_valor(3, 1, 5)
matriz3.definir_valor(3, 2, 6)

print("Matriz 1:")
print(matriz1)
print("Matriz 3:")
print(matriz3)
produto_matrizes = matriz1.multiplicar_matriz(matriz3)
print("Produto das matrizes 1 e 3:")
print(produto_matrizes)