import math

class PoligonoIrregular:
    def __init__(self, vertices):
        self.vertices = vertices  # Lista de coordenadas dos vértices [(x1, y1), (x2, y2), ...]

    def calcular_distancia(self, ponto1, ponto2):
        """
        Calcula a distância entre dois pontos representados por tuplas (x, y).
        """
        return math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)

    @property
    def perimetro(self):
        """
        Calcula o perímetro do polígono irregular.
        """
        perimetro = 0
        num_vertices = len(self.vertices)

        for i in range(num_vertices):
            ponto_atual = self.vertices[i]
            ponto_seguinte = self.vertices[(i + 1) % num_vertices]
            perimetro += self.calcular_distancia(ponto_atual, ponto_seguinte)

        return perimetro

    @property
    def area(self):
        """
        Calcula a área do polígono irregular usando a fórmula do determinante.
        """
        area = 0
        num_vertices = len(self.vertices)

        for i in range(num_vertices):
            ponto_atual = self.vertices[i]
            ponto_seguinte = self.vertices[(i + 1) % num_vertices]
            area += (ponto_atual[0] * ponto_seguinte[1]) - (ponto_atual[1] * ponto_seguinte[0])

        return 0.5 * abs(area)

# Exemplo de uso para um polígono irregular com vértices [(0, 0), (4, 0), (2, 3), (1, 1)]
vertices_poligono = [(0, 0), (4, 0), (2, 3), (1, 1)]
poligono_irregular = PoligonoIrregular(vertices_poligono)
print("Polígono Irregular:")
print("Perímetro:", poligono_irregular.perimetro)
print("Área:", poligono_irregular.area)
