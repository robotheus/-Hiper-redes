import json
import networkx as nx
import hypernetx as hnx
import hypernetx.algorithms.hypergraph_modularity as hmod
import matplotlib.pyplot as plt
from cdlib import evaluation, NodeClustering


with open('Dataset/dataset.json') as file:
    dataset = json.load(file)


def graph_network(year: int = None, all: bool = None):
    graph = nx.Graph()
    titles = []
    
    for data in dataset:
        graph.add_node(data["Pessoa autora"])
        
        if data["Titulo"] not in titles:
            titles.append(data["Titulo"])

    for title in titles:
        matching_authors = [item["Pessoa autora"] for item in dataset if item["Titulo"] == title]
        
        for i in range(len(matching_authors)):
            for j in range(i + 1, len(matching_authors)):
                author1 = matching_authors[i]
                author2 = matching_authors[j]

                if author1 != author2: 
                    if not graph.has_edge(author1, author2):
                        graph.add_edge(author1, author2, weight=1)
                    else:
                        graph[author1][author2]['weight'] += 1

    return graph


def centralidadeG(graph : nx.Graph):
    CG = nx.degree_centrality(graph)
    print("CG-G calculada!")
    
    CI = nx.betweenness_centrality(graph)
    print("CI-G calculada!")
    
    CP = nx.closeness_centrality(graph)
    print("CP-G calculada!")
    
    EV = nx.eigenvector_centrality(graph, max_iter=1000)
    print("CEV-G calculada!")

    return CG, CI, CP, EV


def centralidade_G(G, diretorio):
    CG, CI, CP, EV = centralidadeG(G)

    with open(str(diretorio) + '/Grafo/CG-G.json', 'w') as arquivo:
        json.dump(CG, arquivo)

    with open(str(diretorio) + '/Grafo/CI-G.json', 'w') as arquivo:
        json.dump(CI, arquivo)

    with open(str(diretorio) + '/Grafo/CP-G.json', 'w') as arquivo:
        json.dump(CP, arquivo)

    with open(str(diretorio) + '/Grafo/EV-G.json', 'w') as arquivo:
        json.dump(EV, arquivo)


def comunidades_G(G):
    auxG = grafo_equivalente(G, 1, False)
    comunidades = nx.community.louvain_communities(auxG)

    print(f'{len(comunidades)} comunidades detectadas no grafo com LOUVAIN!')
    
    conjuntos_json = json.dumps([list(conjunto) for conjunto in comunidades])

    with open('Resultados/Grafo/Comunidades-G.json', 'w') as f:
        f.write(conjuntos_json)

    return comunidades


def hypergraph_network(year: int = None, all: bool = None):
    titles_authors = {}
    
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

def degree_centrality_hg(hg, diretorio, s):
    auxHG = hg.get_linegraph(s=s)
    
    n = auxHG.number_of_edges() # n é o número de hiperarestas
    hiperarestas = []

    # seleciono as arestas que estao no caminho s
    for x in auxHG.edges():
        if x[0] not in hiperarestas:
            hiperarestas.append(x[0])
        
        if x[1] not in hiperarestas:
            hiperarestas.append(x[1])

    degrees = {}
    
    #calculo os graus de cada vertice nessas aretas
    for x in hiperarestas:
        for y in hg.edges[x]:
            if y not in degrees:
                degrees[y] = 1
            else:
                g = degrees[y]
                degrees[y] = g + 1
    
    for x in degrees.items():
        degrees[x[0]] = x[1] / n
    
    with open(str(diretorio) + '/Hipergrafo/CG-HG-s=' + str(s) + '.json', 'w') as arquivo:
        json.dump(degrees, arquivo)

    print("CG-HG-s=" + str(s) + " calculada!")
    

def centralidade_HG(linegraph, diretorio, s):

    CI = nx.betweenness_centrality(linegraph)

    with open(str(diretorio) + '/Hipergrafo/CI-HG-s=' + str(s) + '.json', 'w') as arquivo:
        json.dump(CI, arquivo)

    print("CI-HG-s=" + str(s) + " calculada!")

    CP = nx.closeness_centrality(linegraph)

    with open(str(diretorio) + '/Hipergrafo/CP-HG-s=' + str(s) + '.json', 'w') as arquivo:
        json.dump(CP, arquivo)
    
    print("CP-HG-s=" + str(s) + " calculada!")

def comunidades_HG(HG):
    K = hmod.kumar(HG)
    
    total = 0
    for x in K:
        total += len(x)

    #print("O número total de vértices na comunidade do hipergrafo é:", total)
    #print("O número total de vértices no hipergrafo é: ", HG.number_of_nodes())

    verticesHG = []
    verticesCM = []
    
    for x in K:
        for y in x:
            verticesCM.append(y)
    
    for x in HG.nodes():
        verticesHG.append(x)
    
    sumidos = []
    for x in verticesHG:
        if x not in verticesCM:
            sumidos.append(x)
    
    aux = HG.remove(keys = sumidos, level = 1)
    #print("O número total de vértices no hipergrafo é: ", aux.number_of_nodes())

    L = hmod.last_step(aux, A = K, wdc=hmod.linear)
    
    conjuntos_json = json.dumps([list(conjunto) for conjunto in L])

    with open('Resultados/Hipergrafo/Comunidades-HG.json', 'w') as f:
        f.write(conjuntos_json)
    
    print(f'{len(L)} comunidades detectadas no hipergrafo com KUMAR!')


def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dicionario = json.load(arquivo)
        return dicionario
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return None

def plot_resultados(dicionario, title, color, legenda):
    chaves_ordenadas = sorted(dicionario, key=dicionario.get, reverse=True)
    valores_ordenados = [dicionario[chave] for chave in chaves_ordenadas]

    top_10_chaves = chaves_ordenadas[:20]
    top_10_valores = valores_ordenados[:20]

    plt.figure(figsize=(8, 6))
    plt.bar(top_10_chaves, top_10_valores, color=color, width=0.3)
    plt.ylabel('Score')
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(legenda)

def plot_resultados2(dicionario1, dicionario2, dicionario3, dicionario4, title, color, diretorio):
    chaves_ordenadas = sorted(dicionario1, key=dicionario1.get, reverse=True)
    valores_ordenados = [dicionario1[chave] for chave in chaves_ordenadas]

    top_10_chaves = chaves_ordenadas[:10]
    top_10_valores = valores_ordenados[:10]

    valores_dicionario2 = []
    valores_dicionario3 = []
    valores_dicionario4 = []

    for chave in top_10_chaves:
        valores_dicionario2.append(dicionario2.get(chave, 0))
        valores_dicionario3.append(dicionario3.get(chave, 0))
        valores_dicionario4.append(dicionario4.get(chave, 0))

    plt.figure(figsize=(10, 6))
    bar_width = 0.2
    index = range(len(top_10_chaves))

    plt.bar(index, top_10_valores, color=color[0], width=bar_width, label='Grafo')
    plt.bar([i + bar_width for i in index], valores_dicionario2, color=color[1], width=bar_width, label='Hipergrafo (s=1)')
    plt.bar([i + 2*bar_width for i in index], valores_dicionario3, color=color[2], width=bar_width, label='Hipergrafo (s=2)')
    plt.bar([i + 3*bar_width for i in index], valores_dicionario4, color=color[3], width=bar_width, label='Hipergrafo (s=3)')

    plt.ylabel('Score')
    plt.title(title)
    plt.xticks([i + 1.5*bar_width for i in index], top_10_chaves, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig(diretorio)
    plt.show()

def grafo_equivalente(G: nx.Graph, s: int, sozinhos : bool):
    auxG = nx.Graph()

    if sozinhos:
        for x in G.nodes():
            auxG.add_node(x)

    for u, v, data in G.edges(data=True):
        if data['weight'] >= s:
            auxG.add_edge(u, v, weight=data['weight'])

    return auxG


def grafos_iguais(G1, G2):
    if set(G1.nodes) == set(G2.nodes) and set(G1.edges) == set(G2.edges):
        return True
    else:
        return False


def ordena(dicionario):
    return dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))


def overlapping_comunidades(com1, com2):
    HG = hypergraph_network()
    auxHG = HG.get_linegraph(edges=False, s=1)
    G = graph_network()
    
    aux1 = NodeClustering(com1, G)
    aux2 = NodeClustering(com2, auxHG)
    
    return evaluation.overlapping_normalized_mutual_information_MGH(aux1, aux2)

def comunidades_eventos():
    eventos = {}
    
    for data in dataset:
        if data["Evento"] not in eventos:
            eventos[data["Evento"]] = []
            eventos[data["Evento"]].append(data["Pessoa autora"])
        else:
            eventos[data["Evento"]].append(data["Pessoa autora"])
    
    aux = []

    for x in eventos.values():
        aux.append(x)

    print(eventos.keys())
    return aux