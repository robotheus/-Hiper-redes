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

colors = ["red", "blue", "orange", "green"]

functions.plot_resultados2(CEN_G_G, 
                          CEN_HG_G_S1,
                          CEN_HG_G_S2,
                          CEN_HG_G_S3,
                          "Degree centrality", colors, 
                          "Gráficos/CG.png")

functions.plot_resultados2(CEN_G_I, 
                          CEN_HG_I_S1,
                          CEN_HG_I_S2,
                          CEN_HG_I_S3,
                          "Betweenness centrality", colors, 
                          "Gráficos/CI.png")

functions.plot_resultados2(CEN_G_P, 
                          CEN_HG_P_S1,
                          CEN_HG_P_S2,
                          CEN_HG_P_S3,
                          "Closeness centrality", colors, 
                          "Gráficos/CP.png")