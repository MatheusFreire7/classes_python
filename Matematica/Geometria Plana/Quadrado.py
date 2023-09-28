import math

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    @property
    def area(self):
        return self.lado**2

    @property
    def perimetro(self):
        return 4 * self.lado

    @property
    def diagonal(self):
        return math.sqrt(2) * self.lado

    @property
    def semi_perimetro(self):
        return 2 * self.lado

    @property
    def raio_circunscrito(self):
        return self.lado / 2

    @property
    def raio_inscrito(self):
        return self.lado / (2 * math.sqrt(2))

    @property
    def angulo_interior(self):
        return 90  # Ângulo interno em graus

    @property
    def angulo_exterior(self):
        return 90  # Ângulo externo em graus

    @property
    def altura(self):
        return self.lado

    @property
    def apotema(self):
        return self.lado / 2

    def calcular_area_setor_circular(self, angulo_em_graus):
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.area
        else:
            return "Ângulo inválido"

    def calcular_comprimento_arco(self, angulo_em_graus):
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * (math.pi * self.diagonal)
        else:
            return "Ângulo inválido"

quadrado = Quadrado(3)
print("Quadrado:")
print("Área:", quadrado.area)
print("Perímetro:", quadrado.perimetro)
print("Diagonal:", quadrado.diagonal)
print("Semi-Perímetro:", quadrado.semi_perimetro)
print("Raio Circunscrito:", quadrado.raio_circunscrito)
print("Raio Inscrito:", quadrado.raio_inscrito)
print("Ângulo Interior:", quadrado.angulo_interior)
print("Ângulo Exterior:", quadrado.angulo_exterior)
print("Altura:", quadrado.altura)
print("Apótema:", quadrado.apotema)
print("Área do Setor Circular (90 graus):", quadrado.calcular_area_setor_circular(90))
print("Comprimento de Arco (90 graus):", quadrado.calcular_comprimento_arco(90))

