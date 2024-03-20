import functions

HG = functions.hypergraph_network(year = None, all = True)
G = functions.graph_network(year = None, all = True)

for x in range(2,4):
    auxHG = HG.get_linegraph(edges = False, s = x)
    functions.centralidadeHG(auxHG, "Resultados-Equivalencia", x)

    auxG = functions.grafo_equivalente(G, x)
    functions.centralidadeG(auxG, "Resultados-Equivalencia")

    CEN_G_G     = functions.ler_json("Resultados-Equivalencia/Grafo/CG-G.json")
    CEN_G_I     = functions.ler_json("Resultados-Equivalencia/Grafo/CI-G.json")
    CEN_G_P     = functions.ler_json("Resultados-Equivalencia/Grafo/CP-G.json")
    CEN_G_EV    = functions.ler_json("Resultados-Equivalencia/Grafo/EV-G.json")

    CEN_HG_G     = functions.ler_json("Resultados-Equivalencia/Hipergrafo/CG-HG-s=" + str(x) + ".json")
    CEN_HG_I     = functions.ler_json("Resultados-Equivalencia/Hipergrafo/CI-HG-s=" + str(x) + ".json")
    CEN_HG_P     = functions.ler_json("Resultados-Equivalencia/Hipergrafo/CP-HG-s=" + str(x) + ".json")
    
    functions.plot_resultados(CEN_G_G, "Degree centrality (Grafo s = " + str(x) + ")", 'skyblue')
    functions.plot_resultados(CEN_G_I, "Betweenness centrality (Grafo s = " + str(x) + ")", "salmon")
    functions.plot_resultados(CEN_G_P, "Closeness centrality (Grafo s = " + str(x) + ")", "khaki")
    functions.plot_resultados(CEN_G_EV, "Eigenvector centrality (Grafo s = " + str(x) + ")", "mediumseagreen")

    functions.plot_resultados(CEN_HG_G, "Degree centrality (Hipergrafo s = " + str(x) + ")", 'skyblue')
    functions.plot_resultados(CEN_HG_I, "Betweenness centrality (Hipergrafo s = " + str(x) + ")", "salmon")
    functions.plot_resultados(CEN_HG_P, "Closeness centrality (Hipergrafo s = " + str(x) + ")", "khaki")
    