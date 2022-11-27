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