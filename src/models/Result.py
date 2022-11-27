class Result:
    def __init__(self, country, division, total_medals):
        self.country = country;
        self.division = division;
        self.total_medals = total_medals;

    def __str__(self):
        return f"country: {self.country}, division:{self.division}, total_medals:{self.total_medals}"
        