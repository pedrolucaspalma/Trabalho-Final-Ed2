
#def run_algorithms(olympics):
   # print("========Medalhas do Egito========")
   # country1 = olympics.find_node_bfs("Egypt")
    #for result in country1.results:
        #print(result)

   # print("========Medalhas do Brasil========")
   # country2 = olympics.find_node_bfs("Brazil")
    #for result in country2.results:
        #print(result)

   # print("========Países que competiram no Arco e Flecha========")
    #discipline1 = olympics.find_node_bfs("Archery")
    #for result in discipline1.results:
       # print(result)

def menu(olympics):
    discipline_name: str = ""
    country_name: str = ""
    option: int = -1 

    while(option != 0):
        print_options(discipline_name, country_name)
        option = int(input("Opção: "))
        match option:
            case 1:
                discipline_name = str(input("modalidade: "))
                if discipline_name != olympics.verify_discipline_name(discipline_name):
                    print("Modalidade não existe")
            case 2:
                country_name = str(input("País: "))
                if country_name != olympics.verify_country_name(country_name):
                    print("País não existe")    
            case 3:
                print("País",country_name, "encontrado\n")
                print("Modalidade",discipline_name, "encontrada\n")
            case 4:
                olympics.performance(country_name, discipline_name)
            case 5:
                discipline_name = ""
                country_name = ""
            

def print_options(discipline_name, country_name):
    print("****************************************************************************************")
    print("Busca em Grafos Olimpíadas:")
    print("Opções:")
    print(f'1-Definir Modalidade. Atual: {discipline_name}') if discipline_name != "" else print(f'1-Definir Modalidade.')
    print(f'2-Definir País. Atual: {country_name}') if country_name != "" else print(f'2-Definir País')
    print("3-Buscar\n4-Mostrar Resultado de Busca\n5-Limpar inputs anteriores\n\n0- Encerrar Programa.")
            

