
def run_algorithms(olympics):
    print("========Medalhas do Egito========")
    country1 = olympics.find_node_bfs("Egypt")
    for result in country1.results:
        print(result)

    print("========Medalhas do Brasil========")
    country2 = olympics.find_node_bfs("Brazil")
    for result in country2.results:
        print(result)

    print("========Países que competiram no Arco e Flecha========")
    discipline1 = olympics.find_node_bfs("Archery")
    for result in discipline1.results:
        print(result)