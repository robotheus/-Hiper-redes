import functions

CEN_G_G     = functions.ler_json("Resultados/Grafo/CG-G.json")
CEN_G_I     = functions.ler_json("Resultados/Grafo/CI-G.json")
CEN_G_P     = functions.ler_json("Resultados/Grafo/CP-G.json")
CEN_G_EV    = functions.ler_json("Resultados/Grafo/EV-G.json")

COM_G       = functions.ler_json("Resultados/Grafo/Comunidades-G.json")

CEN_HG_G_S1 = functions.ler_json("Resultados/Hipergrafo/CG-HG-s=1.json")
CEN_HG_I_S1 = functions.ler_json("Resultados/Hipergrafo/CI-HG-s=1.json")
CEN_HG_P_S1 = functions.ler_json("Resultados/Hipergrafo/CP-HG-s=1.json")

CEN_HG_G_S2 = functions.ler_json("Resultados/Hipergrafo/CG-HG-s=2.json")
CEN_HG_I_S2 = functions.ler_json("Resultados/Hipergrafo/CI-HG-s=2.json")
CEN_HG_P_S2 = functions.ler_json("Resultados/Hipergrafo/CP-HG-s=2.json")

CEN_HG_G_S3 = functions.ler_json("Resultados/Hipergrafo/CG-HG-s=3.json")
CEN_HG_I_S3 = functions.ler_json("Resultados/Hipergrafo/CI-HG-s=3.json")
CEN_HG_P_S3 = functions.ler_json("Resultados/Hipergrafo/CP-HG-s=3.json")

COM_HG      = functions.ler_json("Resultados/Hipergrafo/Comunidades-HG.json")

functions.plot_resultados(CEN_G_G, "Degree centrality (Grafo)", 'skyblue')
functions.plot_resultados(CEN_G_I, "Betweenness centrality (Grafo)", "salmon")
functions.plot_resultados(CEN_G_P, "Closeness centrality (Grafo)", "khaki")
functions.plot_resultados(CEN_G_EV, "Eigenvector centrality (Grafo)", "mediumseagreen")

functions.plot_resultados(CEN_HG_G_S1, "Degree centrality (Hipergrafo com s = 1)", 'skyblue')
functions.plot_resultados(CEN_HG_I_S1, "Betweenness centrality (Hipergrafo com s = 1)", "salmon")
functions.plot_resultados(CEN_HG_P_S1, "Closeness centrality (Hipergrafo s = 1)", "khaki")

functions.plot_resultados(CEN_HG_G_S2, "Degree centrality (Hipergrafo com s = 2)", 'skyblue')
functions.plot_resultados(CEN_HG_I_S2, "Betweenness centrality (Hipergrafo com s = 2)", "salmon")
functions.plot_resultados(CEN_HG_P_S2, "Closeness centrality (Hipergrafo s = 2)", "khaki")

functions.plot_resultados(CEN_HG_G_S3, "Degree centrality (Hipergrafo com s = 3)", 'skyblue')
functions.plot_resultados(CEN_HG_I_S3, "Betweenness centrality (Hipergrafo com s = 3)", "salmon")
functions.plot_resultados(CEN_HG_P_S3, "Closeness centrality (Hipergrafo s = 3)", "khaki")