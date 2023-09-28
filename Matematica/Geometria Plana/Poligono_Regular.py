import math

class PoligonoRegular:
    def __init__(self, n, comprimento_lado):
        self.n = n  # Número de lados
        self.comprimento_lado = comprimento_lado  # Comprimento de cada lado

    @property
    def perimetro(self):
        """
        Calcula o perímetro do polígono regular.
        """
        return self.n * self.comprimento_lado

    @property
    def apotema(self):
        """
        Calcula o comprimento da apótema do polígono regular.
        """
        apotema = self.comprimento_lado / (2 * math.tan(math.pi / self.n))
        return apotema

    @property
    def area(self):
        """
        Calcula a área do polígono regular.
        """
        area = 0.5 * self.n * self.comprimento_lado * self.apotema
        return area

    @property
    def angulo_interior(self):
        """
        Calcula o ângulo interno entre dois lados adjacentes do polígono regular.
        """
        return (self.n - 2) * 180 / self.n

    @property
    def angulo_exterior(self):
        """
        Calcula o ângulo exterior entre dois lados adjacentes do polígono regular.
        """
        return 360 / self.n

    @property
    def raio_circunscrito(self):
        """
        Calcula o raio da circunferência circunscrita ao polígono regular.
        """
        raio_circunscrito = (self.comprimento_lado / 2) / math.sin(math.pi / self.n)
        return raio_circunscrito

    @property
    def raio_inscrito(self):
        """
        Calcula o raio da circunferência inscrita no polígono regular.
        """
        raio_inscrito = (self.comprimento_lado / 2) / math.tan(math.pi / self.n)
        return raio_inscrito

# Exemplo de uso para um hexágono regular (6 lados) com comprimento de lado de 4 unidades
hexagono = PoligonoRegular(6, 4)
print("Hexágono Regular:")
print("Perímetro:", hexagono.perimetro)
print("Apótema:", hexagono.apotema)
print("Área:", hexagono.area)
print("Ângulo Interior:", hexagono.angulo_interior)
print("Ângulo Exterior:", hexagono.angulo_exterior)
print("Raio Circunscrito:", hexagono.raio_circunscrito)
print("Raio Inscrito:", hexagono.raio_inscrito)
