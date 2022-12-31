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

        def find_country(self, country_name):
            for country in self.countries:
                if country.name == country_name: return country

        def find_discipline(self, discipline_name):
            for discipline in self.disciplines:
                if discipline.name == discipline_name: return discipline

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

            nx.draw_networkx(
                G=graph,
                node_color=colors,
                node_size=150,
                width=0.5,
                font_size=9
                )
            plt.show()