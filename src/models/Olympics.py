import networkx as nx
import matplotlib.pyplot as plt

def return_name_from_object(obj):
    return obj.name
class Olympics:
        def __init__(self):
            self.countries = [];
            self.disciplines = [];
            self.results = []

        def add_country(self, country):
            self.countries.append(country);

        def add_discipline(self, discipline):
            self.disciplines.append(discipline);

        def add_result(self, result):
            self.results.append(result)

        def create_nodes(self, graph):
            colors = []
            
            for country in self.countries:
                graph.add_node(country.name)
                colors.append("green")

            for discipline in self.disciplines:
                graph.add_node(discipline.name)
                colors.append("blue")

            return colors

        def create_edges(self, graph):
            for result in self.results:
                graph.add_edge(result.country.name, result.discipline.name, weight=result.total_medals)

        def visualize(self):
            graph = nx.Graph()

            colors = self.create_nodes(graph)
            self.create_edges(graph)

            nx.draw_networkx(G=graph, node_color=colors)
            plt.show()