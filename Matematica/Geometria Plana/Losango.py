import math

class Losango:
    def __init__(self, diagonal_maior, diagonal_menor, lado):
        self.diagonal_maior = diagonal_maior
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    @property
    def area(self):
        return 0.5 * self.diagonal_maior * self.diagonal_menor

    @property
    def perimetro(self):
        return 4 * self.lado

    @property
    def diagonal(self):
        return math.sqrt(self.diagonal_maior**2 + self.diagonal_menor**2)

    @property
    def semi_perimetro(self):
        return 2 * self.lado

    def calcular_angulo(self):
        return math.degrees(math.atan2(self.diagonal_menor / 2, self.diagonal_maior / 2))

    def calcular_inscrito_circunscrito_ratio(self):
        return self.diagonal_menor / self.diagonal_maior

    def calcular_altura(self):
        return 2 * self.area / self.diagonal_maior

losango = Losango(8, 6, 5)
print("Losango:")
print("Área:", losango.area)
print("Perímetro:", losango.perimetro)
print("Diagonal:", losango.diagonal)
print("Semi-Perímetro:", losango.semi_perimetro)
print("Ângulo:", losango.calcular_angulo())
print("Razão entre Diagonais:", losango.calcular_inscrito_circunscrito_ratio())
print("Altura:", losango.calcular_altura())
