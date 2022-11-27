class Discipline:
    def __init__(self, name):
        self.name = name;
        self.results = []

    def add_result(self, results):
        self.results.append(results)

    def __str__(self):
        return f"Discipline <name: {self.name}, results:{self.results}>"