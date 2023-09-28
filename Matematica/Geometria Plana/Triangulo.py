import math

class Triangulo:
    def __init__(self, base=None, altura=None, lado1=None, lado2=None, lado3=None):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

        if base is None or altura is None:
            self.base = 0
            self.altura = 0

        if lado1 is None:
            self.lado1 = 0

        if lado2 is None:
            self.lado2 = 0

        if lado3 is None:
            self.lado3 = 0

    @property
    def area(self):
        if self.base > 0 and self.altura > 0:
            return 0.5 * self.base * self.altura
        else:
            return "Impossível calcular"

    @property
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def classificar(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Triângulo Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"

    def calcular_altura(self):
        if self.base > 0 and self.area != "Impossível calcular":
            return 2 * self.area / self.base
        else:
            return "Impossível calcular"

    def calcular_area_equilatero(self):
        if self.lado1 > 0 and self.lado1 == self.lado2 == self.lado3:
            return (math.sqrt(3) / 4) * self.lado1**2
        else:
            return "Impossível calcular"

    def calcular_diagonal(self):
        if self.base > 0 and self.altura > 0:
            hipotenusa = math.sqrt(self.base**2 + self.altura**2)
            return hipotenusa
        else:
            return "Impossível calcular"

    @property
    def semi_perimetro(self):
        return 0.5 * self.perimetro

    def calcular_angulo(self, lado):
        if lado == "lado1":
            return math.degrees(math.acos((self.lado2**2 + self.lado3**2 - self.lado1**2) / (2 * self.lado2 * self.lado3)))
        elif lado == "lado2":
            return math.degrees(math.acos((self.lado1**2 + self.lado3**2 - self.lado2**2) / (2 * self.lado1 * self.lado3)))
        elif lado == "lado3":
            return math.degrees(math.acos((self.lado1**2 + self.lado2**2 - self.lado3**2) / (2 * self.lado1 * self.lado2)))
        else:
            return "Lado inválido"

    def calcular_raio_circunscrito(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            return (self.lado1 * self.lado2 * self.lado3) / (4 * self.area)
        else:
            return "Impossível calcular"

    def calcular_area_heron(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            s = self.semi_perimetro
            return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        else:
            return "Impossível calcular"
        
    def calcular_incentro(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            s = self.semi_perimetro
            incenter_radius = math.sqrt(((s - self.lado1) * (s - self.lado2) * (s - self.lado3)) / s)
            incenter_x = (self.lado1 * self.lado2) / (self.lado1 + self.lado2 + self.lado3)
            incenter_y = (self.lado1 * self.lado3) / (self.lado1 + self.lado2 + self.lado3)
            return f"Incentro: ({incenter_x}, {incenter_y}), Raio: {incenter_radius}"
        else:
            return "Impossível calcular"

    def calcular_excentros(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            excenter_radius = self.area / self.semi_perimetro  # Raio dos excentros
            excenter_x1 = 0  # Coordenadas do excentro correspondente ao lado 1
            excenter_y1 = (2 * self.area) / self.lado1
            excenter_x2 = (2 * self.area) / self.lado2  # Coordenadas do excentro correspondente ao lado 2
            excenter_y2 = 0
            excenter_x3 = (2 * self.area) / self.lado3  # Coordenadas do excentro correspondente ao lado 3
            excenter_y3 = (2 * self.area) / self.lado3
            return [
                f"Excentro 1: ({excenter_x1}, {excenter_y1}), Raio: {excenter_radius}",
                f"Excentro 2: ({excenter_x2}, {excenter_y2}), Raio: {excenter_radius}",
                f"Excentro 3: ({excenter_x3}, {excenter_y3}), Raio: {excenter_radius}"
            ]
        else:
            return "Impossível calcular"

    def calcular_inradius(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            return self.area / self.semi_perimetro
        else:
            return "Impossível calcular"

    def calcular_circumradius(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            return (self.lado1 * self.lado2 * self.lado3) / (4 * self.area)
        else:
            return "Impossível calcular"
        
    def calcular_menor_lado(self):
        return min(self.lado1, self.lado2, self.lado3)

    def calcular_maior_lado(self):
        return max(self.lado1, self.lado2, self.lado3)

    def calcular_inclinacao(self):
        if self.base > 0 and self.altura > 0:
            return math.degrees(math.atan(self.altura / self.base))
        else:
            return "Impossível calcular"

    def calcular_raio_circunscrito_inscrito_ratio(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            circumradius = self.calcular_circumradius()
            inradius = self.calcular_inradius()
            if inradius != "Impossível calcular" and circumradius != "Impossível calcular":
                return circumradius / inradius
        return "Impossível calcular"

    def calcular_lado_faltante(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            return max(self.lado1, self.lado2, self.lado3) - self.perimetro + min(self.lado1, self.lado2, self.lado3)
        else:
            return "Impossível calcular"
        
    def calcular_mediana(self, lado):
        if lado == "lado1":
            return 0.5 * math.sqrt(2 * self.lado2**2 + 2 * self.lado3**2 - self.lado1**2)
        elif lado == "lado2":
            return 0.5 * math.sqrt(2 * self.lado1**2 + 2 * self.lado3**2 - self.lado2**2)
        elif lado == "lado3":
            return 0.5 * math.sqrt(2 * self.lado1**2 + 2 * self.lado2**2 - self.lado3**2)
        else:
            return "Lado inválido"

    def calcular_mediana_ratio(self, lado):
        if lado == "lado1":
            return 0.5 * math.sqrt(2 * self.lado2**2 + 2 * self.lado3**2 - self.lado1**2) / self.lado1
        elif lado == "lado2":
            return 0.5 * math.sqrt(2 * self.lado1**2 + 2 * self.lado3**2 - self.lado2**2) / self.lado2
        elif lado == "lado3":
            return 0.5 * math.sqrt(2 * self.lado1**2 + 2 * self.lado2**2 - self.lado3**2) / self.lado3
        else:
            return "Lado inválido"

    def calcular_incenter_x(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            return (self.lado1 * 0 + self.lado2 * self.lado3) / (self.lado1 + self.lado2 + self.lado3)

    def calcular_incenter_y(self):
        if self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0:
            return (self.lado1 * self.lado3 * self.altura) / (self.lado1 + self.lado2 + self.lado3)

    def calcular_altura_em_relacao_a_lado(self, lado):
        if lado == "lado1":
            return (2 * self.area) / self.lado1
        elif lado == "lado2":
            return (2 * self.area) / self.lado2
        elif lado == "lado3":
            return (2 * self.area) / self.lado3
        else:
            return "Lado inválido"
        
#Exemplo de Uso:

# Triângulo com base, altura e lados
triangulo = Triangulo(base=4, altura=3, lado1=3, lado2=4, lado3=5)
print("Triângulo:")
print("Área:", triangulo.area)
print("Perímetro:", triangulo.perimetro)
print("Classificação:", triangulo.classificar())
print("Altura:", triangulo.calcular_altura())
print("Diagonal:", triangulo.calcular_diagonal())
print("Semi-Perímetro:", triangulo.semi_perimetro)
print("Ângulo do lado 1:", triangulo.calcular_angulo("lado1"))
print("Ângulo do lado 2:", triangulo.calcular_angulo("lado2"))
print("Ângulo do lado 3:", triangulo.calcular_angulo("lado3"))
print("Raio da circunferência circunscrita:", triangulo.calcular_raio_circunscrito())
print("Área calculada com fórmula de Heron:", triangulo.calcular_area_heron())