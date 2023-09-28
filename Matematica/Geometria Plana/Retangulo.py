import math

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    @property
    def area(self):
        return self.comprimento * self.largura

    @property
    def perimetro(self):
        return 2 * (self.comprimento + self.largura)

    @property
    def diagonal(self):
        return math.sqrt(self.comprimento**2 + self.largura**2)

    @property
    def semi_perimetro(self):
        return self.comprimento + self.largura

    def calcular_raio_circunscrito(self):
        return 0.5 * math.sqrt(self.comprimento**2 + self.largura**2)

    def calcular_raio_inscrito(self):
        return 0.5 * min(self.comprimento, self.largura)

    def calcular_angulo_interior(self):
        return math.degrees(math.atan2(self.largura, self.comprimento))

    def calcular_angulo_exterior(self):
        return 90 - self.calcular_angulo_interior()

    def calcular_altura(self):
        return self.area / self.largura if self.largura != 0 else "Indefinido"

    def calcular_apotema(self):
        return 0.5 * min(self.comprimento, self.largura)

retangulo = Retangulo(4, 6)
print("Retângulo:")
print("Área:", retangulo.area)
print("Perímetro:", retangulo.perimetro)
print("Diagonal:", retangulo.diagonal)
print("Semi-Perímetro:", retangulo.semi_perimetro)
print("Raio Circunscrito:", retangulo.calcular_raio_circunscrito())
print("Raio Inscrito:", retangulo.calcular_raio_inscrito())
print("Ângulo Interior:", retangulo.calcular_angulo_interior())
print("Ângulo Exterior:", retangulo.calcular_angulo_exterior())
print("Altura:", retangulo.calcular_altura())
print("Apótema:", retangulo.calcular_apotema())
