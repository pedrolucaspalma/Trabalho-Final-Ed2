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

        def visualize(self):
            graph = nx.Graph()

            countries = self.countries
            graph.add_nodes_from(map(lambda country:  (country.name, {"color": "red"}), countries))

            disciplines = self.disciplines
            graph.add_nodes_from(map(lambda discipline: (discipline.name, {"color":"green"}), disciplines))

            # results = self.results
            # graph.add_weighted_edges_from(map(lambda result: [result.country, result.discipline, result.total_medals], results))

            nx.draw_networkx(G=graph)
            plt.show()
            
        # def find_country(self, country_name):