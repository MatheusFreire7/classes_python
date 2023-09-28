import matplotlib.pyplot as plt

class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return -1  # A altura de um nó vazio é -1
        return no.altura


    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_esquerda(self, z):
        if z is None or z.direita is None:  # Verifique se a subárvore direita existe
            return z

        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    
    def rotacao_direita(self, y):
        if y is None or y.esquerda is None:  # Verifique se a subárvore esquerda existe
            return y

        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def inserir(self, no, chave):
        if no is None:
            return NoAVL(chave)

        if chave < no.chave:
            no.esquerda = self.inserir(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self.inserir(no.direita, chave)
        else:
            return no  # Não permitir chaves duplicadas

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

        balanceamento = self.fator_balanceamento(no)

        # Casos de rotação para manter o balanceamento
        if balanceamento > 1:
            if chave < no.esquerda.chave:
                return self.rotacao_direita(no)
            else:
                no.esquerda = self.rotacao_esquerda(no.esquerda)
                return self.rotacao_direita(no)
        if balanceamento < -1:
            if chave > no.direita.chave:
                return self.rotacao_esquerda(no)
            else:
                no.direita = self.rotacao_direita(no.direita)
                return self.rotacao_esquerda(no)

        return no

    def inserir_chave(self, chave):
        self.raiz = self.inserir(self.raiz, chave)

    def buscar(self, chave):
        return self._buscar_recursivamente(self.raiz, chave)

    def _buscar_recursivamente(self, no, chave):
        if no is None:
            return False
        if chave == no.chave:
            return True
        elif chave < no.chave:
            return self._buscar_recursivamente(no.esquerda, chave)
        else:
            return self._buscar_recursivamente(no.direita, chave)

    def remover(self, chave):
        self.raiz = self._remover_recursivamente(self.raiz, chave)

    def _remover_recursivamente(self, no, chave):
        if no is None:
            return no

        if chave < no.chave:
            no.esquerda = self._remover_recursivamente(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_recursivamente(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            no.chave = self._minimo_valor(no.direita)
            no.direita = self._remover_recursivamente(no.direita, no.chave)

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

        balanceamento = self.fator_balanceamento(no)

        # Casos de rotação para manter o balanceamento
        if balanceamento > 1:
            if self.fator_balanceamento(no.esquerda) >= 0:
                return self.rotacao_direita(no)
            else:
                no.esquerda = self.rotacao_esquerda(no.esquerda)
                return self.rotacao_direita(no)
        if balanceamento < -1:
            if self.fator_balanceamento(no.direita) <= 0:
                return self.rotacao_esquerda(no)
            else:
                no.direita = self.rotacao_direita(no.direita)
                return self.rotacao_esquerda(no)

        return no

    def minimo(self):
        return self._minimo_valor(self.raiz)

    def _minimo_valor(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no.chave

    def maximo(self):
        return self._maximo_valor(self.raiz)

    def _maximo_valor(self, no):
        while no.direita is not None:
            no = no.direita
        return no.chave

    def altura_arvore(self):
        return self.altura(self.raiz)

    def percorrer_in_order(self, no):
        if no:
            self.percorrer_in_order(no.esquerda)
            print(no.chave, end=" ")
            self.percorrer_in_order(no.direita)

    def percorrer_in_order_raiz(self):
        self.percorrer_in_order(self.raiz)

    def esta_vazia(self):
        return self.raiz is None
    
    def contar_nos(self):
        return self._contar_nos_recursivamente(self.raiz)

    def _contar_nos_recursivamente(self, no):
        if no is None:
            return 0
        return 1 + self._contar_nos_recursivamente(no.esquerda) + self._contar_nos_recursivamente(no.direita)
    
    def listar_valores(self):
        valores = []
        self._listar_valores_recursivamente(self.raiz, valores)
        return valores

    def _listar_valores_recursivamente(self, no, lista):
        if no:
            self._listar_valores_recursivamente(no.esquerda, lista)
            lista.append(no.chave)
            self._listar_valores_recursivamente(no.direita, lista)

    #Verica se a árvore é uma Árvore de Busca Binária (BST
    def e_bst(self):
        return self._e_bst_recursivamente(self.raiz, float('-inf'), float('inf'))

    def _e_bst_recursivamente(self, no, min_valor, max_valor):
        if no is None:
            return True

        if no.chave < min_valor or no.chave > max_valor:
            return False

        return (self._e_bst_recursivamente(no.esquerda, min_valor, no.chave - 1) and
                self._e_bst_recursivamente(no.direita, no.chave + 1, max_valor))
    
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
            plt.text(x, y, str(no.chave), ha='center', va='center')

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
arvore_avl = ArvoreAVL()
arvore_avl.inserir_chave(5)
arvore_avl.inserir_chave(15)
arvore_avl.inserir_chave(25)

# Criar uma árvore AVL vazia
arvore_vazia = ArvoreAVL()

# Verificar se a árvore AVL está vazia
print("Árvore AVL vazia?", arvore_vazia.esta_vazia())  # True
print("Árvore AVL não vazia?", arvore_avl.esta_vazia())  # False

# Contar o número de nós na árvore
print("Número de nós na árvore AVL:", arvore_avl.contar_nos())  # Deve ser 3

# Listar os valores da árvore em ordem
print("Valores da árvore AVL em ordem:", arvore_avl.listar_valores())  # Deve ser [5,15,25]

# Verificar se a árvore é uma Árvore de Busca Binária (BST)
print("É uma BST?", arvore_avl.e_bst())  # True

# Inserir chaves repetidas (não permitidas)
arvore_avl.inserir_chave(10)
print("Valores da árvore AVL após inserção duplicada:", arvore_avl.listar_valores())  # Deve ser [5, 10, 15, 25]

# Remover a raiz
arvore_avl.remover(10)
print("Valores da árvore AVL após remover a raiz:", arvore_avl.listar_valores())  # Deve ser [5, 15, 25]

# Verificar altura da árvore
print("Altura da árvore AVL:", arvore_avl.altura_arvore())  # Deve ser 2

arvore_avl.exibir_graficamente_arvore()