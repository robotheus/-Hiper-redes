import json
import hypernetx as hnx
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import igraph as ig

with open('Dataset/dataset.json') as file:
    dataset = json.load(file)

def hypergraph_network(year: int = None, evento = None):
    titles_authors = {}
    
    if year:
        for data in dataset:
            if data["Ano"] == year:                  
                if data["Titulo"] not in titles_authors:
                    titles_authors[data["Titulo"]] = []
                    titles_authors[data["Titulo"]].append(data["Pessoa autora"])
                else:
                    titles_authors[data["Titulo"]].append(data["Pessoa autora"])
    elif evento:
        for data in dataset:
            if data["Evento"] == evento:                  
                if data["Titulo"] not in titles_authors:
                    titles_authors[data["Titulo"]] = []
                    titles_authors[data["Titulo"]].append(data["Pessoa autora"])
                else:
                    titles_authors[data["Titulo"]].append(data["Pessoa autora"])
    else:
        for data in dataset:
            if data["Titulo"] not in titles_authors:
                titles_authors[data["Titulo"]] = []
                titles_authors[data["Titulo"]].append(data["Pessoa autora"])
            else:
                titles_authors[data["Titulo"]].append(data["Pessoa autora"])

    for x in titles_authors:
        titles_authors[x] = tuple(titles_authors[x])

    H = hnx.Hypergraph(titles_authors)

    return H

def plot(H, diretorio, year : int = None):
    plt.subplots(figsize=(8,6))

    kwargs = {"k" : 0.1, "iterations" : 100}
    
    color_map = {
        'BRASNAM': '#007FFF',  # Vermelho
        'WPERFORMANCE': '#FFD700',  # Amarelo dourado
        'SBCUP': '#00C957',  # Verde limão
        'SEMISH': '#FF2400',  # Azul forte
        'BRESCI': '#8A2BE2',  # Violeta
        'CTD': '#FF1493',  # Rosa profundo
        'WEI': '#00FFFF',  # Ciano
        'WIT': '#FF4500',  # Laranja vermelho
        'CTIC': '#32CD32',  # Verde-lima
        'WCAMA': '#4169E1'  # Azul-royal
    }

    color_map2 = {
        2013: '#007FFF',  # Vermelho
        2014: '#FFD700',  # Amarelo dourado
        2015: '#00C957',  # Verde limão
        2016: '#FF2400',  # Azul forte
        2017: '#8A2BE2',  # Violeta
        2018: '#FF1493',  # Rosa profundo
        2019: '#00FFFF',  # Ciano
        2020: '#FF4500',  # Laranja vermelho
        2021: '#32CD32',  # Verde-lima
        2022: '#4169E1'  # Azul-royal
    }
    
    color_title_event = {}

    for data in dataset:
        if data["Titulo"] not in color_title_event:
            color_title_event[data["Titulo"]] = color_map[data["Evento"]]
    
    color_title_year = {}

    for data in dataset:
        if data["Titulo"] not in color_title_year:
            color_title_year[data["Titulo"]] = color_map2[data["Ano"]]

    edges_kwargs={
        #'facecolors': color_title,
        'edgecolors': color_map["BRASNAM"]
    }

    pos = hnx.drawing.draw(H, node_radius=0.3,
                with_edge_labels=False,
                with_edge_counts=True, 
                with_node_counts=False,
                with_node_labels=False,
                layout=nx.spring_layout,
                layout_kwargs=kwargs,
                edges_kwargs=edges_kwargs
                )
    
    legend = []
    
    for node, color in color_map2.items():
        if node == 'BRASNAM':
            legend.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=5, label='Evento BRASNAM'))
        else:
            # Para outros nós, adicione normalmente
            legend.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=5, label=node))
        
    plt.legend(handles=legend, loc='lower left', fontsize='small')
    
    if year:
        plt.savefig(str(diretorio) + str(year) + ".png")
    else:
        plt.savefig(diretorio)

def componente_gig(arestas : list):
    titles_authors = {}
    
    for data in dataset:
        if data["Titulo"] in arestas:
            if data["Titulo"] not in titles_authors:
                titles_authors[data["Titulo"]] = []
                titles_authors[data["Titulo"]].append(data["Pessoa autora"])
            else:
                titles_authors[data["Titulo"]].append(data["Pessoa autora"])

    for x in titles_authors:
        titles_authors[x] = tuple(titles_authors[x])

    H = hnx.Hypergraph(titles_authors)

    return H

def componentes(hypergraph : hnx.Hypergraph):
    componentes_conectados = list(hypergraph.s_connected_components(edges=True, return_singletons = False))
    print(str(len(componentes_conectados)) + " componentes conectados.")

    componente_gigante = max(componentes_conectados, key=len)
    H = componente_gig(componente_gigante)    
    print(f'{H.number_of_nodes()} nodos e {H.number_of_edges()} arestas no componente gigante.')

    return H

H = hypergraph_network(evento="BRASNAM")
print(H.number_of_nodes(), H.number_of_edges())
plot(H, "Plot/Brasnam_todos_anos_3.png")

"""year = 2013

for x in range(1, 11):
    H = hypergraph_network(year=year)
    plot(H, "Plot/n-colapsado/", year)
    year = year + 1"""