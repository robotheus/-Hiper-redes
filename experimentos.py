import functions

G = functions.graph_network(year = None, all = True)
functions.centralidadeG(G)
functions.comunidadesG(G)
    
HG = functions.hypergraph_network(year = None, all = True)
functions.centralidadeHG(HG)
functions.comunidadesHG(HG)

