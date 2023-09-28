import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def area(self):
        return math.pi * self.raio**2

    @property
    def perimetro(self):
        return 2 * math.pi * self.raio

    @property
    def diagonal(self):
        return 2 * self.raio

    @property
    def semi_perimetro(self):
        return math.pi * self.raio

    def calcular_circunferencia(self):
        return math.pi * self.raio

    def calcular_diametro(self):
        return 2 * self.raio

    def calcular_setor_circular(self, angulo_em_graus):
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.area
        else:
            return "Ângulo inválido"

    def calcular_comprimento_arco(self, angulo_em_graus):
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.perimetro
        else:
            return "Ângulo inválido"

    def calcular_raio_inscrito(self):
        return self.raio / 2

    def calcular_raio_circunscrito(self):
        return self.raio

    def calcular_area_setor_circular(self, angulo_em_graus):
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.area
        else:
            return "Ângulo inválido"

    def calcular_area_anular(self, angulo_em_graus):
        if 0 <= angulo_em_graus <= 360:
            raio_interno = self.raio / 2
            raio_externo = self.raio
            area_setor_externo = self.calcular_area_setor_circular(angulo_em_graus)
            area_setor_interno = math.pi * raio_interno**2 * (angulo_em_graus / 360)
            return area_setor_externo - area_setor_interno
        else:
            return "Ângulo inválido"

    def calcular_setor_circular_3_pontos(self, angulo_em_graus):
        if 0 <= angulo_em_graus <= 360:
            return (angulo_em_graus / 360) * self.perimetro
        else:
            return "Ângulo inválido"

circulo = Circulo(5)
print("Círculo:")
print("Área:", circulo.area)
print("Perímetro:", circulo.perimetro)
print("Diagonal:", circulo.diagonal)
print("Semi-Perímetro:", circulo.semi_perimetro)
print("Circunferência:", circulo.calcular_circunferencia())
print("Diâmetro:", circulo.calcular_diametro())
print("Setor Circular (60 graus):", circulo.calcular_setor_circular(60))
print("Comprimento de Arco (60 graus):", circulo.calcular_comprimento_arco(60))
print("Raio Inscrito:", circulo.calcular_raio_inscrito())
print("Raio Circunscrito:", circulo.calcular_raio_circunscrito())
print("Área Setor Circular (120 graus):", circulo.calcular_area_setor_circular(120))
print("Área Anular (120 graus):", circulo.calcular_area_anular(120))
print("Setor Circular 3 Pontos (60 graus):", circulo.calcular_setor_circular_3_pontos(60))
