import math

class Pentagono:
    def __init__(self, lado):
        self.lado = lado

    @property
    def area(self):
        """
        Calcula a área do pentágono regular.
        """
        return (5 * self.lado**2) / (4 * math.tan(math.pi / 5))

    @property
    def perimetro(self):
        """
        Calcula o perímetro do pentágono regular.
        """
        return 5 * self.lado

    @property
    def diagonal(self):
        """
        Calcula a diagonal do pentágono regular (distância entre dois vértices não adjacentes).
        """
        return self.lado * math.sqrt(5 + 2 * math.sqrt(5))

    @property
    def apotema(self):
        """
        Calcula a apótema do pentágono regular (distância do centro ao centro de um lado).
        """
        return self.lado / (2 * math.tan(math.pi / 5))

    @property
    def angulo_interior(self):
        return 108

    @property
    def angulo_exterior(self):
        return 72

    def calcular_area_setor_circular(self, angulo_em_graus):
        """
        Calcula a área de um setor circular do pentágono regular com base em um ângulo central em graus.
        """
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.area
        else:
            return "Ângulo inválido"

    def calcular_comprimento_arco(self, angulo_em_graus):
        """
        Calcula o comprimento do arco de um setor circular do pentágono regular com base em um ângulo central em graus.
        """
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.perimetro
        else:
            return "Ângulo inválido"

pentagono = Pentagono(4)
print("Pentágono Regular:")
print("Área:", pentagono.area)
print("Perímetro:", pentagono.perimetro)
print("Diagonal:", pentagono.diagonal)
print("Apótema:", pentagono.apotema)
print("Ângulo Interior:", pentagono.angulo_interior)
print("Ângulo Exterior:", pentagono.angulo_exterior)
print("Área de Setor Circular (60 graus):", pentagono.calcular_area_setor_circular(60))
print("Comprimento de Arco (60 graus):", pentagono.calcular_comprimento_arco(60))