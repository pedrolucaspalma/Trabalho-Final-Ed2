import networkx as nx
import matplotlib.pyplot as plt

from models.Country import Country
from models.Discipline import Discipline

class Olympics:
        """ 
        Classe base para armazenar os dados do grafo em memória.

        A implementação do grafo foi feita através de uma matriz de adjacências, em que a classe Olympics
        possui duas listas que armazenam os nós (que são instâncias de objetos das classes Country e Discipline).

        Dessa forma, cada nó (Country ou Discipline) possui uma lista de Results, que representa quantas medalhas cada país recebeu naquela modalidade (no grafo, são arestas com pesos). 

        Possui métodos para buscar, adicionar e remover nós, além de uma visualização gráfica com as bibliotecas networkx e pyplot. 
        """
        def __init__(self):
            # Os vetores de países e modalidades são meramente auxiliares para facilitar a construção da ilustração do grafo com cores separadas.
            self.countries = []; 
            self.disciplines = [];
            # Vetor utilizado para armazenar as arestas totais do grafo. Novamente, apenas usado para construção da ilustração do grafo.
            self.results = [];

            # Vetor principal utilizado para armazenar os nós do grafo para utilizar nos algoritmos de DFS e BFS
            self.total_nodes = [];

        def get_results():
            return results
        
        def add_country(self, country):
            self.countries.append(country);
            self.total_nodes.append(country);

        def add_discipline(self, discipline):
            self.disciplines.append(discipline);
            self.total_nodes.append(discipline);

        def add_result(self, result):
            self.results.append(result)

        def verify_country_name(self, country_name) -> str:
            for country in self.countries:
                if country.name == country_name: return country.name

        def verify_discipline_name(self, discipline_name) -> str:
            for discipline in self.disciplines:
                if discipline.name == discipline_name: return discipline.name

        def find_country(self, country_name):
            """
            Parameters
            ----------
            country_name: str
                O nome do país

            Busca simples em Array para encontrar um país a partir da classe Olympics.
            """
            for country in self.countries:
                if country.name == country_name: return country

        def find_discipline(self, discipline_name):
            """
            Parameters
            ----------
            discipline_name: str
                O nome da modalidade

            Busca simples em Array para encontrar uma modalidade a partir da classe Olympics
            """
            for discipline in self.disciplines:
                if discipline.name == discipline_name: return discipline
        
        def performance(self, country_name: str, discipline_name: str) -> None:
            if(country_name =="" or discipline_name == ""): 
                return print('Voce precisa escolher um pais e uma modalidade primeiro!')
            
            performance_results = []
            for result in self.results:
                if result.discipline.name == discipline_name and result.country.name == country_name:
                    performance_results.push(result)

            if(len(performance_results) == 0):
                print(f'{country_name} nunca competiu em {discipline_name}.')

            for result in performance_results:
                print(result)


        def find_node_bfs(self, node_name):
            """
            Parameters
            ----------
            node_name: str
                O nome do vértice (País ou Modalidade)

            Busca por um vertice utilizando busca por largura (Breadth First Search).
            """
            if len(self.total_nodes) == 0:
                return print("O grafo não possui vértices!")

            initial_node = self.total_nodes[0]
            queue = []
            visited = []

            queue.append(initial_node)
            visited.append(initial_node)

            while queue:
                current = queue.pop(0)

                for result in current.results:
                    if isinstance(current, Discipline):
                        if result.country.name == node_name: return result.country

                        if result.country not in visited:
                            visited.append(result.country)
                            queue.append(result.country)
                        
                    if isinstance(current, Country):
                        if result.discipline.name == node_name: return result.discipline

                        if result.discipline not in visited:
                            visited.append(result.discipline)
                            queue.append(result.discipline)

            print("Vértice não encontrado.")

        def find_node_dfs(self, node_name):
            """
            Parameters
            ----------
            node_name: str
                O nome do vértice (País ou Modalidade)

            Busca por um vertice utilizando busca por profundidade (Depth First Search).
            """

           # A standard Depth-First Search implementation puts every vertex of the graph
           #  into one in all 2 categories: 1) Visited 2) Not Visited. 

            not_visited = []
            visited = []
           
           # The only purpose of this algorithm is to visit all the vertex of the graph avoiding cycles.

           #1.We will start by putting any one of the graph's vertex on top of the stack.
            initial_node = self.total_nodes[0]
            not_visited.append(initial_node)
            
           #2.After that take the top item of the stack and add it to the visited list of the vertex

            visited.append(not_visited.pop)

            #3.Next, create a list of that adjacent node of the vertex. Add the ones which aren't in the visited list of vertexes to the top of the stack.

            #4.Lastly, keep repeating steps 2 and 3 until the stack is empty
        # TODO

        def delete_node(self, node_name):
            """
            Parameters
            ----------
            node_name: str
                O nome do vértice (País ou Modalidade)

            Remoção de um vertice.
            """
        #TODO

        def create_nodes(self, graph):
            colors = []
            for country in self.countries:
                graph.add_node(country.name)
                colors.append("green")

            for discipline in self.disciplines:
                graph.add_node(discipline.name)
                colors.append("blue")

            #TODO Chamar o método plt.show() de novo com o grafo atualizado
            return colors

        def create_edges(self, graph):
            for result in self.results:
                graph.add_edge(result.country.name, result.discipline.name, weight=result.total_medals)

        def visualize(self):
            graph = nx.Graph()

            plt.figure(figsize=(18,18))

            colors = self.create_nodes(graph)
            self.create_edges(graph)

            nx.draw_networkx(
                graph,
                node_color=colors,
                node_size=150,
                width=0.5,
                font_size=9
                )
            plt.show()