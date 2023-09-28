import math
import matplotlib.pyplot as plt
import numpy as np

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GeometriaAnalitica:
    @staticmethod
    def distancia(ponto1, ponto2):
        dx = ponto1.x - ponto2.x
        dy = ponto1.y - ponto2.y
        return math.sqrt(dx ** 2 + dy ** 2)

    @staticmethod
    def ponto_medio(ponto1, ponto2):
        x = (ponto1.x + ponto2.x) / 2
        y = (ponto1.y + ponto2.y) / 2
        return f"({x}, {y})"

    @staticmethod
    def sao_colineares(ponto1, ponto2, ponto3):
        det = (ponto1.x * (ponto2.y - ponto3.y) +
               ponto2.x * (ponto3.y - ponto1.y) +
               ponto3.x * (ponto1.y - ponto2.y))
        return det == 0

    @staticmethod
    def angulo_entre_vetores(ponto1, ponto2, ponto3, ponto4):
        dx1 = ponto2.x - ponto1.x
        dy1 = ponto2.y - ponto1.y
        dx2 = ponto4.x - ponto3.x
        dy2 = ponto4.y - ponto3.y

        produto_escalar = dx1 * dx2 + dy1 * dy2
        norma_vetor1 = math.sqrt(dx1 ** 2 + dy1 ** 2)
        norma_vetor2 = math.sqrt(dx2 ** 2 + dy2 ** 2)

        cos_theta = produto_escalar / (norma_vetor1 * norma_vetor2)
        return math.degrees(math.acos(cos_theta))

    @staticmethod
    def area_triangulo(ponto1, ponto2, ponto3):
        """
        Calcula a área de um triângulo formado por três pontos.
        """
        return 0.5 * abs((ponto1.x * (ponto2.y - ponto3.y) +
                          ponto2.x * (ponto3.y - ponto1.y) +
                          ponto3.x * (ponto1.y - ponto2.y)))

    @staticmethod
    def ponto_reflexao(ponto1, ponto2):
        """
        Encontra o ponto de reflexão de um ponto em relação a uma linha definida por dois pontos.
        """
        dx = ponto2.x - ponto1.x
        dy = ponto2.y - ponto1.y
        return f"({ponto2.x + dx}, {ponto2.y + dy})"

    @staticmethod
    def distancia_ponto_reta(ponto, ponto1, ponto2):
        """
        Calcula a distância entre um ponto e uma reta definida por dois pontos.
        """
        numerador = abs((ponto2.x - ponto1.x) * (ponto1.y - ponto.y) - (ponto1.x - ponto.x) * (ponto2.y - ponto1.y))
        denominador = math.sqrt((ponto2.x - ponto1.x) ** 2 + (ponto2.y - ponto1.y) ** 2)
        return numerador / denominador

    @staticmethod
    def intersecao_reta_reta(ponto1, ponto2, ponto3, ponto4):
        """
        Encontra o ponto de interseção entre duas retas definidas por dois pontos cada.
        Retorna None se as retas são paralelas.
        """
        det = (ponto1.x - ponto2.x) * (ponto3.y - ponto4.y) - (ponto1.y - ponto2.y) * (ponto3.x - ponto4.x)
        if det == 0:
            return None  # Retas paralelas

        px = ((ponto1.x * ponto2.y - ponto1.y * ponto2.x) * (ponto3.x - ponto4.x) -
              (ponto1.x - ponto2.x) * (ponto3.x * ponto4.y - ponto3.y * ponto4.x)) / det

        py = ((ponto1.x * ponto2.y - ponto1.y * ponto2.x) * (ponto3.y - ponto4.y) -
              (ponto1.y - ponto2.y) * (ponto3.x * ponto4.y - ponto3.y * ponto4.x)) / det

        return f"({px}, {py})"

    @staticmethod
    def equacao_reta(ponto1, ponto2):
        """
        Encontra a equação da reta que passa por dois pontos no formato y = mx + b.
        """
        if ponto1.x == ponto2.x:
            return None  # A reta é vertical, não pode ser representada como y = mx + b

        m = (ponto2.y - ponto1.y) / (ponto2.x - ponto1.x)
        b = ponto1.y - m * ponto1.x
        return (m, b)

    @staticmethod
    def ponto_proximo_reta(ponto, ponto1, ponto2):
        """
        Encontra o ponto mais próximo de uma reta definida por dois pontos a partir de um ponto dado.
        """
        if ponto1.x == ponto2.x:
            # A reta é vertical
            return Ponto(ponto1.x, ponto.y)
        else:
            m, b = GeometriaAnalitica.equacao_reta(ponto1, ponto2)
            x = (ponto.x + m * ponto.y - m * b) / (m ** 2 + 1)
            y = (m * (ponto.x + m * ponto.y) + b) / (m ** 2 + 1)
            return f"({x}, {y})"
        
    @staticmethod
    def comprimento_circunferencia(raio):
        """
        Calcula o comprimento de uma circunferência com base no raio.
        """
        return 2 * math.pi * raio

    @staticmethod
    def area_circulo(raio):
        """
        Calcula a área de um círculo com base no raio.
        """
        return math.pi * (raio ** 2)

    @staticmethod
    def ponto_circunferencia(angulo, raio, centro):
        """
        Calcula as coordenadas de um ponto em uma circunferência com base no ângulo, raio e centro.
        """
        x = centro.x + raio * math.cos(math.radians(angulo))
        y = centro.y + raio * math.sin(math.radians(angulo))
        return f"({x}, {y})"

    @staticmethod
    def intersecao_circunferencias(centro1, raio1, centro2, raio2):
        """
        Encontra os pontos de interseção entre duas circunferências.
        Retorna None se não houver interseção.
        """
        d = GeometriaAnalitica.distancia(centro1, centro2)
        
        if d > raio1 + raio2 or d < abs(raio1 - raio2):
            return None  # Não há interseção
        
        a = (raio1 ** 2 - raio2 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(raio1 ** 2 - a ** 2)
        
        x2 = centro1.x + a * (centro2.x - centro1.x) / d
        y2 = centro1.y + a * (centro2.y - centro1.y) / d
        
        x3_1 = x2 + h * (centro2.y - centro1.y) / d
        y3_1 = y2 - h * (centro2.x - centro1.x) / d
        
        x3_2 = x2 - h * (centro2.y - centro1.y) / d
        y3_2 = y2 + h * (centro2.x - centro1.x) / d
        
        ponto1 = Ponto(x3_1, y3_1)
        ponto2 = Ponto(x3_2, y3_2)
        
        return f"A({x3_1}, {y3_1}); B({x3_2},{y3_2})"
    
    @staticmethod
    def area_elipse(semi_eixo_maior, semi_eixo_menor):
        """
        Calcula a área de uma elipse com base nos semieixos maior e menor.
        """
        return math.pi * semi_eixo_maior * semi_eixo_menor

    @staticmethod
    def ponto_elipse(angulo, semi_eixo_maior, semi_eixo_menor, centro):
        """
        Calcula as coordenadas de um ponto em uma elipse com base no ângulo, semieixos, e centro.
        """
        x = centro.x + semi_eixo_maior * math.cos(math.radians(angulo))
        y = centro.y + semi_eixo_menor * math.sin(math.radians(angulo))
        return f"({x}, {y})"

    @staticmethod
    def area_retangulo(ponto1, ponto2):
        """
        Calcula a área de um retângulo com base em dois vértices opostos.
        """
        lado1 = abs(ponto1.x - ponto2.x)
        lado2 = abs(ponto1.y - ponto2.y)
        return lado1 * lado2

    @staticmethod
    def perimetro_retangulo(ponto1, ponto2):
        """
        Calcula o perímetro de um retângulo com base em dois vértices opostos.
        """
        lado1 = abs(ponto1.x - ponto2.x)
        lado2 = abs(ponto1.y - ponto2.y)
        return 2 * (lado1 + lado2)
    
    @staticmethod
    def area_poligono(vertices):
        """
        Calcula a área de um polígono convexo com base em suas coordenadas dos vértices.
        """
        n = len(vertices)
        area = 0
        for i in range(n):
            x1, y1 = vertices[i].x, vertices[i].y
            x2, y2 = vertices[(i + 1) % n].x, vertices[(i + 1) % n].y
            area += (x1 * y2 - x2 * y1)
        return 0.5 * abs(area)
    
    @staticmethod
    def volume_cilindro(raio_base, altura):
        """
        Calcula o volume de um cilindro com base no raio da base e altura.
        """
        return math.pi * (raio_base ** 2) * altura

    @staticmethod
    def volume_cone(raio_base, altura):
        """
        Calcula o volume de um cone com base no raio da base e altura.
        """
        return (1/3) * math.pi * (raio_base ** 2) * altura

    @staticmethod
    def volume_esfera(raio):
        """
        Calcula o volume de uma esfera com base no raio.
        """
        return (4/3) * math.pi * (raio ** 3)

    @staticmethod
    def volume_cubo(aresta):
        """
        Calcula o volume de um cubo com base na aresta.
        """
        return aresta ** 3
    
    @staticmethod
    def volume_paralelepipedo(comprimento, largura, altura):
        """
        Calcula o volume de um paralelepípedo com base no comprimento, largura e altura.
        """
        return comprimento * largura * altura

    @staticmethod
    def volume_prisma(base_area, altura):
        """
        Calcula o volume de um prisma com base na área da base e altura.
        """
        return base_area * altura
    
    @staticmethod
    def equacao_reta_duas_pontos(ponto1, ponto2):
        """
        Encontra a equação da reta que passa por dois pontos no formato ax + by + c = 0.
        """
        a = ponto2.y - ponto1.y
        b = ponto1.x - ponto2.x
        c = (ponto1.x * ponto2.y) - (ponto2.x * ponto1.y)
        return (a, b, c)
    
    @staticmethod
    def area_quadrilatero(ponto1, ponto2, ponto3, ponto4):
        """
        Calcula a área de um quadrilátero formado por quatro pontos.
        """
        area_tri1 = GeometriaAnalitica.area_triangulo(ponto1, ponto2, ponto3)
        area_tri2 = GeometriaAnalitica.area_triangulo(ponto1, ponto3, ponto4)
        return area_tri1 + area_tri2
    
    def desenhar_plano_cartesiano(reta=None, circulo=None, elipse=None, xlim=(-10, 10), ylim=(-10, 10)):
        # Criar uma figura e eixos
        fig, ax = plt.subplots()

        # Definir limites do plano cartesiano
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        # Desenhar reta, se fornecida
        if reta is not None:
            x_reta = [ponto.x for ponto in reta]
            y_reta = [ponto.y for ponto in reta]
            ax.plot(x_reta, y_reta, label='Reta')

        # Desenhar círculo, se fornecido
        if circulo is not None:
            centro = circulo[0]
            raio = circulo[1]
            angulos = np.linspace(0, 2 * np.pi, 100)
            x_circulo = [centro.x + raio * np.cos(theta) for theta in angulos]
            y_circulo = [centro.y + raio * np.sin(theta) for theta in angulos]
            ax.plot(x_circulo, y_circulo, label='Círculo')

        # Desenhar elipse, se fornecida
        if elipse is not None:
            centro = elipse[0]
            semi_eixo_maior = elipse[1]
            semi_eixo_menor = elipse[2]
            angulos = np.linspace(0, 2 * np.pi, 100)
            x_elipse = [centro.x + semi_eixo_maior * np.cos(theta) for theta in angulos]
            y_elipse = [centro.y + semi_eixo_menor * np.sin(theta) for theta in angulos]
            ax.plot(x_elipse, y_elipse, label='Elipse')

        # Legenda
        ax.legend()

        # Exibir o plano cartesiano
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.title('Plano Cartesiano')
        plt.show()


       
# Exemplo de uso:
pontoA = Ponto(1, 2)
pontoB = Ponto(4, 6)
pontoC = Ponto(7, 10)

print("Distância entre A e B:", GeometriaAnalitica.distancia(pontoA, pontoB))
print("Ponto médio entre A e B:", GeometriaAnalitica.ponto_medio(pontoA, pontoB))
print("São colineares A, B e C?", GeometriaAnalitica.sao_colineares(pontoA, pontoB, pontoC))

reta_AB = [Ponto(-2, 3), Ponto(1, -3)]
circulo = [Ponto(0, 0), 3]
elipse = [Ponto(5, -5), 4, 2]

GeometriaAnalitica.desenhar_plano_cartesiano(reta=reta_AB, circulo=circulo, elipse=elipse)