import math

class Hexagono:
    def __init__(self, lado):
        self.lado = lado

    @property
    def area(self):
        """
        Calcula a área do hexágono.
        """
        return (3 * math.sqrt(3) * self.lado**2) / 2

    @property
    def perimetro(self):
        """
        Calcula o perímetro do hexágono.
        """
        return 6 * self.lado

    @property
    def diagonal(self):
        """
        Calcula a diagonal do hexágono (distância entre dois vértices opostos).
        """
        return 2 * self.lado

    @property
    def apotema(self):
        """
        Calcula a apótema do hexágono (distância do centro ao centro de um lado).
        """
        return math.sqrt(3) * self.lado / 2

    @property
    def angulo_interior(self):
        """
        Calcula o ângulo interno entre dois lados adjacentes do hexágono.
        """
        return 120

    @property
    def angulo_exterior(self):
        """
        Calcula o ângulo externo entre dois lados adjacentes do hexágono.
        """
        return 60

    def calcular_area_setor_circular(self, angulo_em_graus):
        """
        Calcula a área de um setor circular do hexágono com base em um ângulo central em graus.
        """
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.area
        else:
            return "Ângulo inválido"

    def calcular_comprimento_arco(self, angulo_em_graus):
        """
        Calcula o comprimento do arco de um setor circular do hexágono com base em um ângulo central em graus.
        """
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.perimetro
        else:
            return "Ângulo inválido"

hexagono = Hexagono(4)
print("Hexágono:")
print("Área:", hexagono.area)
print("Perímetro:", hexagono.perimetro)
print("Diagonal:", hexagono.diagonal)
print("Apótema:", hexagono.apotema)
print("Ângulo Interior:", hexagono.angulo_interior)
print("Ângulo Exterior:", hexagono.angulo_exterior)
print("Área de Setor Circular (60 graus):", hexagono.calcular_area_setor_circular(60))
print("Comprimento de Arco (60 graus):", hexagono.calcular_comprimento_arco(60))