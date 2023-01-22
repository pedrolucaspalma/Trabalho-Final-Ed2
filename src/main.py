from get_data import datarows

from models.Country import Country
from models.Discipline import Discipline
from models.Result import Result
from models.Olympics import Olympics

from displaying_algorithms import run_algorithms

olympics = Olympics()

# Preenchendo o grafo com vértices:
for row in datarows:
    country_name = row['Country']
    discipline_name = row['Discipline']
    total_medals = row['Medal']
    olympics_ed = row['Year']

    country = olympics.find_country(country_name);
    if bool(country) is False:
        country = Country(country_name)
        olympics.add_country(country)
    
    discipline = olympics.find_discipline(discipline_name)
    if bool(discipline) is False:
        discipline = Discipline(discipline_name)
        olympics.add_discipline(discipline)
    

    result = Result(country, discipline, row['Medal'], row['Year'])
    country.add_result(result)
    discipline.add_result(result)
    olympics.add_result(result)

# Testando os algoritmos de busca:
run_algorithms(olympics)

# Criando a visualização
olympics.visualize()

