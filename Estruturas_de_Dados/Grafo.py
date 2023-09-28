import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        """Adiciona um vértice ao grafo."""
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def remover_vertice(self, vertice):
        """Remove um vértice do grafo e todas as arestas associadas a ele."""
        if vertice in self.vertices:
            del self.vertices[vertice]
            for v in self.vertices:
                self.vertices[v] = [vizinho for vizinho in self.vertices[v] if vizinho != vertice]

    def adicionar_aresta(self, vertice1, vertice2):
        """Adiciona uma aresta entre dois vértices."""
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append(vertice2)
            self.vertices[vertice2].append(vertice1)
    
    def remover_aresta(self, vertice1, vertice2):
        """Remove uma aresta entre dois vértices."""
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1] = [vizinho for vizinho in self.vertices[vertice1] if vizinho != vertice2]
            self.vertices[vertice2] = [vizinho for vizinho in self.vertices[vertice2] if vizinho != vertice1]

    def sao_vizinhos(self, vertice1, vertice2):
        """Verifica se dois vértices são vizinhos (conectados por uma aresta)."""
        return vertice1 in self.vertices and vertice2 in self.vertices[vertice1]

    def mostrar_grafo(self):
        """Exibe o grafo na forma de vértices e suas arestas (vizinhos)."""
        for vertice, vizinhos in self.vertices.items():
            vizinhos_str = ", ".join(vizinhos)
            print(f"{vertice}: {vizinhos_str}")

    def obter_grau(self, vertice):
        """Obtém o grau de um vértice (número de arestas conectadas a ele)."""
        if vertice in self.vertices:
            return len(self.vertices[vertice])
        else:
            return 0

    def obter_vertices(self):
        """Retorna uma lista de todos os vértices no grafo."""
        return list(self.vertices.keys())

    def verificar_existencia_vertice(self, vertice):
        """Verifica se um vértice existe no grafo."""
        return vertice in self.vertices

    def contar_vertices(self):
        """Conta o número de vértices no grafo."""
        return len(self.vertices)

    def verificar_grafo_vazio(self):
        """Verifica se o grafo está vazio (sem vértices)."""
        return len(self.vertices) == 0
    
    def obter_arestas(self):
        """Retorna uma lista de todas as arestas no grafo."""
        arestas = []
        for vertice, vizinhos in self.vertices.items():
            for vizinho in vizinhos:
                if (vertice, vizinho) not in arestas and (vizinho, vertice) not in arestas:
                    arestas.append((vertice, vizinho))
        return arestas

    def verificar_grafo_conexo(self):
        """Verifica se o grafo é conexo (todos os vértices são alcançáveis a partir de qualquer vértice)."""
        if not self.vertices:
            return True
        visitados = set()
        fila = [list(self.vertices.keys())[0]]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                visitados.add(vertice)
                fila.extend(vizinho for vizinho in self.vertices[vertice] if vizinho not in visitados)
        return len(visitados) == len(self.vertices)
    
    def plot_grafo(self):
        """Exibe o grafo graficamente usando o Matplotlib."""
        G = nx.Graph()
        for vertice, vizinhos in self.vertices.items():
            for vizinho in vizinhos:
                G.add_edge(vertice, vizinho)

        pos = nx.spring_layout(G)  # Define a posição dos vértices
        labels = {vertice: vertice for vertice in G.nodes()}  # Rótulos dos vértices

        nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color="skyblue", font_size=12, font_color="black")
        plt.title("Grafo")
        plt.show()


# Exemplo de uso:
grafo = Grafo()

grafo.adicionar_vertice("A")
grafo.adicionar_vertice("B")
grafo.adicionar_vertice("C")
grafo.adicionar_vertice("D")

grafo.adicionar_aresta("A", "B")
grafo.adicionar_aresta("B", "C")
grafo.adicionar_aresta("C", "D")
grafo.adicionar_aresta("D", "A")

grafo.mostrar_grafo()
grafo.plot_grafo() 

print("Removendo vértice B e sua aresta com C:")
grafo.remover_vertice("B")
grafo.mostrar_grafo()

print("Removendo aresta entre C e D:")
grafo.remover_aresta("C", "D")
grafo.mostrar_grafo()

print("Verificando se A e D são vizinhos:", grafo.sao_vizinhos("A", "D"))
print("Verificando se B e C são vizinhos:", grafo.sao_vizinhos("B", "C"))