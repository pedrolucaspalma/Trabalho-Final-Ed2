class Result:
    def __init__(self, country, discipline, total_medals):
        self.country = country;
        self.discipline = discipline;
        self.total_medals = total_medals;

    def __str__(self):
        return f"{self.country.name} has gotten {self.total_medals} on discipline '{self.discipline.name}'"
        