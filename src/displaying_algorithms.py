
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
    discpline: str = ""
    country: str = ""
    option: int = -1 

    

    while(option != 0):
        print("Busca em Grafos Olimpíadas:\nOpções:\n1-Definir Modalidade\n2-Definir País\n3-Buscar\n4-Mostrar Resultado de Busca")
        option = int(input("Opção: "))
        match option:
            case 1:
                discipline = str(input("modalidade: "))
                if discipline != olympics.verify_discipline_name(discipline):
                    print("Modalidade não existe")
            case 2:
                country = str(input("País: "))
                if country != olympics.verify_country_name(country):
                    print("País não existe")    
            case 3:
                print("País",country, "encontrado\n")
                print("Modalidade",discipline, "encontrada\n")
            case 4:
                olympics.performance(country, discipline)

            
               

