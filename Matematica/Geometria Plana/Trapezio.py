import math

class Trapezio:
    def __init__(self, base_menor, base_maior, altura, lado1, lado2):
        self.base_menor = base_menor
        self.base_maior = base_maior
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    @property
    def area(self):
        return 0.5 * (self.base_menor + self.base_maior) * self.altura

    @property
    def perimetro(self):
        return self.base_menor + self.base_maior + self.lado1 + self.lado2

    @property
    def diagonal(self):
        return math.sqrt(self.lado1**2 + (self.altura**2) * ((self.base_maior - self.base_menor)**2 + self.altura**2) / 4)

    @property
    def semi_perimetro(self):
        return 0.5 * self.perimetro

    def calcular_angulo(self):
        return math.degrees(math.atan2(self.altura, (self.base_maior - self.base_menor) / 2))

    def calcular_mediana(self):
        return 0.5 * (self.base_menor + self.base_maior)

    def calcular_altura_relacao_lados(self):
        return self.altura / self.lado1, self.altura / self.lado2

    def calcular_area_circunscrita(self):
        return math.pi * (self.lado1 + self.lado2) * self.altura

    def calcular_area_inscrita(self):
        return 0.5 * self.base_menor * self.altura

    def calcular_raio_inscrito(self):
        return self.area * 2 / self.perimetro

    def calcular_raio_circunscrito(self):
        return self.base_maior / (2 * math.sin(math.radians(self.calcular_angulo())))

trapezio = Trapezio(4, 6, 3, 4, 5)
print("Trapézio:")
print("Área:", trapezio.area)
print("Perímetro:", trapezio.perimetro)
print("Diagonal:", trapezio.diagonal)
print("Semi-Perímetro:", trapezio.semi_perimetro)
print("Ângulo:", trapezio.calcular_angulo())
print("Mediana:", trapezio.calcular_mediana())
print("Altura em relação aos lados:", trapezio.calcular_altura_relacao_lados())
print("Área circunscrita:", trapezio.calcular_area_circunscrita())
print("Área inscrita:", trapezio.calcular_area_inscrita())
print("Raio inscrito:", trapezio.calcular_raio_inscrito())
print("Raio circunscrito:", trapezio.calcular_raio_circunscrito())