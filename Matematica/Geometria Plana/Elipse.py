import math

class Elipse:
    def __init__(self, semieixo_maior, semieixo_menor):
        self.semieixo_maior = semieixo_maior
        self.semieixo_menor = semieixo_menor

    @property
    def area(self):
        """
        Calcula a área da elipse.
        """
        return math.pi * self.semieixo_maior * self.semieixo_menor

    @property
    def perimetro(self):
        """
        Calcula o perímetro aproximado da elipse (fórmula de Ramanujan).
        """
        a = self.semieixo_maior
        b = self.semieixo_menor
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    @property
    def excentricidade(self):
        """
        Calcula a excentricidade da elipse.
        """
        a = self.semieixo_maior
        b = self.semieixo_menor
        return math.sqrt(1 - (b ** 2) / (a ** 2))

    @property
    def focos(self):
        """
        Calcula as coordenadas dos focos da elipse.
        """
        c = math.sqrt(self.semieixo_maior**2 - self.semieixo_menor**2)
        return (-c, 0), (c, 0)

    def ponto_na_elipse(self, x, y):
        """
        Verifica se um ponto (x, y) está dentro ou na borda da elipse.
        Retorna True se estiver dentro ou na borda, False caso contrário.
        """
        a = self.semieixo_maior
        b = self.semieixo_menor
        return (x ** 2 / a ** 2) + (y ** 2 / b ** 2) <= 1

# Exemplo de uso para uma elipse com semieixos maiores 4 e 2:
elipse = Elipse(4, 2)
print("Elipse:")
print("Área:", elipse.area)
print("Perímetro:", elipse.perimetro)
print("Excentricidade:", elipse.excentricidade)
print("Focos:", elipse.focos)
print("Ponto (2, 1) na elipse:", elipse.ponto_na_elipse(2, 1))
print("Ponto (5, 3) na elipse:", elipse.ponto_na_elipse(5, 3))
