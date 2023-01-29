class Result:
    def __init__(self, country, discipline, total_medals, year):
        self.country = country;
        self.discipline = discipline;
        self.total_medals = total_medals;
        self.year = year

    def __str__(self):
        return f"{self.country.name} conseguiu {self.total_medals} medalhas na modalidade '{self.discipline.name}' nas olimpiadas de '{self.year}'"
        