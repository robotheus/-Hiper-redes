import functions
import networkx as nx

HG = functions.hypergraph_network()
G = functions.graph_network()

print(f"Grafo com {G.number_of_edges()} arestas e {G.number_of_nodes()} vértices")
print(f"Hipergrafo com {HG.number_of_edges()} arestas e {HG.number_of_nodes()} vértices")

for x in range(1,4):
    auxHG = HG.get_linegraph(edges = False, s = x)
    auxG = functions.grafo_equivalente(G, x, True)
    
    print(f"LInegraph com {auxHG.number_of_edges()} arestas e {auxHG.number_of_nodes()} vértices")
    print(f"S-Grafo com {auxG.number_of_edges()} arestas e {auxG.number_of_nodes()} vértices")
    
    functions.centralidade_G(auxG, "Resultados-Equivalencia")
    functions.centralidade_HG(auxHG, "Resultados-Equivalencia", x)

    CEN_G_G     = functions.ler_json("Resultados-Equivalencia/Grafo/CG-G.json")
    CEN_G_I     = functions.ler_json("Resultados-Equivalencia/Grafo/CI-G.json")
    CEN_G_P     = functions.ler_json("Resultados-Equivalencia/Grafo/CP-G.json")
    CEN_G_EV    = functions.ler_json("Resultados-Equivalencia/Grafo/EV-G.json")

    CEN_HG_G     = functions.ler_json("Resultados-Equivalencia/Hipergrafo/CG-HG-s=" + str(x) + ".json")
    CEN_HG_I     = functions.ler_json("Resultados-Equivalencia/Hipergrafo/CI-HG-s=" + str(x) + ".json")
    CEN_HG_P     = functions.ler_json("Resultados-Equivalencia/Hipergrafo/CP-HG-s=" + str(x) + ".json")
    
    functions.plot_resultados(CEN_G_G, "Degree centrality (Grafo s = " + str(x) + ")", 'skyblue', "Gráficos-Equivalencia/Grafos/G-D-S=" + str(x))
    functions.plot_resultados(CEN_G_I, "Betweenness centrality (Grafo s = " + str(x) + ")", "salmon", "Gráficos-Equivalencia/Grafos/G-B-S=" + str(x))
    functions.plot_resultados(CEN_G_P, "Closeness centrality (Grafo s = " + str(x) + ")", "khaki", "Gráficos-Equivalencia/Grafos/G-C-S=" + str(x))
    functions.plot_resultados(CEN_G_EV, "Eigenvector centrality (Grafo s = " + str(x) + ")", "mediumseagreen", "Gráficos-Equivalencia/Grafos/G-EV-S=" + str(x))

    functions.plot_resultados(CEN_HG_G, "Degree centrality (Hipergrafo s = " + str(x) + ")", 'skyblue', "Gráficos-Equivalencia/HIpergrafos/HG-D-S=" + str(x))
    functions.plot_resultados(CEN_HG_I, "Betweenness centrality (Hipergrafo s = " + str(x) + ")", "salmon", "Gráficos-Equivalencia/HIpergrafos/HG-B-S=" + str(x))
    functions.plot_resultados(CEN_HG_P, "Closeness centrality (Hipergrafo s = " + str(x) + ")", "khaki", "Gráficos-Equivalencia/HIpergrafos/HG-C-S=" + str(x))