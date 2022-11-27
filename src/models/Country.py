class Country:
    def __init__(self, name):
        self.name = name;
        self.results = [];

    def __str__(self):
        return f"Country: <name: {self.name}, results:{self.results}>"

    def add_result(self, result):
        self.results = self.results.append(result)

    # def remove_result(self, result):
    #     self.results
        