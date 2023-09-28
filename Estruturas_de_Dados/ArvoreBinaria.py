import matplotlib.pyplot as plt

class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self, raiz):
        self.raiz = NoArvore(raiz)

    def inserir(self, valor):
        self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = NoArvore(valor)
            else:
                self._inserir_recursivamente(no.esquerda, valor)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = NoArvore(valor)
            else:
                self._inserir_recursivamente(no.direita, valor)

    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no, valor):
        if no is None:
            return False
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivamente(no.esquerda, valor)
        else:
            return self._buscar_recursivamente(no.direita, valor)

    def exibir(self):
        self._exibir_recursivamente(self.raiz)

    def _exibir_recursivamente(self, no):
        if no is not None:
            self._exibir_recursivamente(no.esquerda)
            print(no.valor, end=" ")
            self._exibir_recursivamente(no.direita)

    def remover(self, valor):
        self.raiz = self._remover_recursivamente(self.raiz, valor)

    def _remover_recursivamente(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self._remover_recursivamente(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_recursivamente(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            no.valor = self._minimo_valor(no.direita)
            no.direita = self._remover_recursivamente(no.direita, no.valor)

        return no

    def minimo(self):
        return self._minimo_valor(self.raiz)

    def _minimo_valor(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no.valor

    def maximo(self):
        return self._maximo_valor(self.raiz)

    def _maximo_valor(self, no):
        while no.direita is not None:
            no = no.direita
        return no.valor

    def altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, no):
        if no is None:
            return 0
        altura_esquerda = self._calcular_altura(no.esquerda)
        altura_direita = self._calcular_altura(no.direita)
        return max(altura_esquerda, altura_direita) + 1
    
    def is_balanceada(self):
        return self._is_balanceada_recursivamente(self.raiz)

    def _is_balanceada_recursivamente(self, no):
        if no is None:
            return True

        altura_esquerda = self._calcular_altura(no.esquerda)
        altura_direita = self._calcular_altura(no.direita)

        if abs(altura_esquerda - altura_direita) <= 1 and \
           self._is_balanceada_recursivamente(no.esquerda) and \
           self._is_balanceada_recursivamente(no.direita):
            return True

        return False
    
    def is_arvore_de_busca_binaria(self):
        return self._is_arvore_de_busca_binaria_recursivamente(self.raiz, float('-inf'), float('inf'))

    def _is_arvore_de_busca_binaria_recursivamente(self, no, min_valor, max_valor):
        if no is None:
            return True

        if min_valor < no.valor < max_valor and \
           self._is_arvore_de_busca_binaria_recursivamente(no.esquerda, min_valor, no.valor) and \
           self._is_arvore_de_busca_binaria_recursivamente(no.direita, no.valor, max_valor):
            return True

        return False
    
    def exibir_graficamente_arvore(self):
        plt.figure(figsize=(12, 8))
        ax = plt.gca()
        ax.axis('off')
        self._plot_tree(ax, self.raiz, x=0, y=0, horizontal_spacing=2, level=0)
        plt.show()

    def _plot_tree(self, ax, no, x, y, horizontal_spacing, level):
        if no is not None:
            circle = plt.Circle((x, y), 0.5, color='lightblue', fill=True)
            ax.add_patch(circle)
            plt.text(x, y, str(no.valor), ha='center', va='center')

            if no.esquerda is not None:
                next_x = x - horizontal_spacing * 2 ** (max(0, 3 - level))
                next_y = y - 2
                plt.plot([x, next_x], [y, next_y], color='gray', linestyle='-', linewidth=2)
                self._plot_tree(ax, no.esquerda, next_x, next_y, horizontal_spacing, level + 1)

            if no.direita is not None:
                next_x = x + horizontal_spacing * 2 ** (max(0, 3 - level))
                next_y = y - 2
                plt.plot([x, next_x], [y, next_y], color='gray', linestyle='-', linewidth=2)
                self._plot_tree(ax, no.direita, next_x, next_y, horizontal_spacing, level + 1)
    
# Exemplo de uso:
arvore = ArvoreBinaria(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

print("Árvore em ordem:")
arvore.exibir()
print("\nMínimo valor na árvore:", arvore.minimo())
print("Máximo valor na árvore:", arvore.maximo())
print("Altura da árvore:", arvore.altura())

arvore.remover(5)
print("\nÁrvore após a remoção:")
arvore.exibir()

arvore.exibir_graficamente_arvore()