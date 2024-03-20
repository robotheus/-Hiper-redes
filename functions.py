import json
import networkx as nx
import hypernetx as hnx
import hypernetx.algorithms.hypergraph_modularity as hmod
import matplotlib.pyplot as plt
from cdlib import evaluation, algorithms

with open('Dataset/dataset.json') as file:
    dataset = json.load(file)

def graph_network(year: int = None, all: bool = None):
    graph = nx.Graph()
    titles = []
    event = []

    if year:
        for data in dataset:
            if data["Ano"] == year:
                graph.add_node(data["Pessoa autora"])
                titles.append(data["Titulo"])
                event.append(data["Evento"])
        
        for title in titles:
            matching_authors = [item["Pessoa autora"] for item in dataset if item["Titulo"] == title]
            
            evento = [item["Evento"] for item in dataset if item["Titulo"] == title]
            matching_authors.append(evento[0])

            for author1 in matching_authors:
                for author2 in matching_authors:
                    if author1 not in event and author2 not in event and author1 != author2 and not graph.has_edge(author1, author2):
                        graph.add_edge(author1, author2, title=title, 
                                    classe = matching_authors[len(matching_authors) - 1],
                                    weight = 1)
                    elif author1 != author2 and author1 not in event and author2 not in event:
                        p = graph[author1][author2]['weight']
                        graph[author1][author2]['weight'] = p + 1

        return graph

    if all:
        for data in dataset:
            graph.add_node(data["Pessoa autora"])
            titles.append(data["Titulo"])
            event.append(data["Evento"])
        
        for title in titles:
            matching_authors = [item["Pessoa autora"] for item in dataset if item["Titulo"] == title]
            
            evento = [item["Evento"] for item in dataset if item["Titulo"] == title]
            matching_authors.append(evento[0])

            for author1 in matching_authors:
                for author2 in matching_authors:
                    if author1 not in event and author2 not in event and author1 != author2 and not graph.has_edge(author1, author2):
                        graph.add_edge(author1, author2, title=title, 
                                    classe = matching_authors[len(matching_authors) - 1],
                                    weight = 1)
                    elif author1 != author2 and author1 not in event and author2 not in event:
                        p = graph[author1][author2]['weight']
                        graph[author1][author2]['weight'] = p + 1

        return graph



def centrality_graph(graph : nx.Graph):
    CG = nx.degree_centrality(graph)
    CI = nx.betweenness_centrality(graph)
    CP = nx.closeness_centrality(graph)
    EV = nx.eigenvector_centrality(graph)
    
    return CG, CI, CP, EV


def centralidadeG(G, diretorio):
    CG, CI, CP, EV = centrality_graph(G)

    with open(str(diretorio) + '/Grafo/CG-G.json', 'w') as arquivo:
        json.dump(CG, arquivo)

    with open(str(diretorio) + '/Grafo/CI-G.json', 'w') as arquivo:
        json.dump(CI, arquivo)

    with open(str(diretorio) + '/Grafo/CP-G.json', 'w') as arquivo:
        json.dump(CP, arquivo)

    with open(str(diretorio) + '/Grafo/EV-G.json', 'w') as arquivo:
        json.dump(EV, arquivo)

    print("Centralidades do grafo calculadas!")


def comunidadesG(G):
    comunidades = nx.community.louvain_communities(G)

    print(f'{len(comunidades)} comunidades detectadas no grafo!')
    
    conjuntos_json = json.dumps([list(conjunto) for conjunto in comunidades])

    with open('Resultados/Grafo/Comunidades-G.json', 'w') as f:
        f.write(conjuntos_json)

    return comunidades


def hypergraph_network(year: int = None, all: bool = None):
    if year:
        titles_authors = {}
        
        for data in dataset:
            if data["Ano"] == year:
                if data["Titulo"] not in titles_authors:
                    titles_authors[data["Titulo"]] = []
                    titles_authors[data["Titulo"]].append(data["Pessoa autora"])
                else:
                    titles_authors[data["Titulo"]].append(data["Pessoa autora"])

        for x in titles_authors:
            titles_authors[x] = tuple(titles_authors[x])

        H = hnx.Hypergraph(titles_authors)
        
        return H

    if all:
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

def centralidadeHG(linegraph, diretorio, s):
    
    CG = nx.degree_centrality(linegraph)
    
    with open(str(diretorio) + '/Hipergrafo/CG-HG-s=' + str(s) + '.json', 'w') as arquivo:
        json.dump(CG, arquivo)

    print("CG-s=" + str(s) + " calculada!")
    
    CI = nx.betweenness_centrality(linegraph)

    with open(str(diretorio) + '/Hipergrafo/CI-HG-s=' + str(s) + '.json', 'w') as arquivo:
        json.dump(CI, arquivo)

    print("CI-s=" + str(s) + " calculada!")

    CP = nx.closeness_centrality(linegraph)

    with open(str(diretorio) + '/Hipergrafo/CP-HG-s=' + str(s) + '.json', 'w') as arquivo:
        json.dump(CP, arquivo)
    
    print("CP-s=" + str(s) + " calculada!")

def comunidadesHG(HG):
    K = hmod.kumar(HG)
    
    total = 0
    for x in K:
        total += len(x)

    print("O número total de vértices na comunidade do hipergrafo é:", total)
    print("O número total de vértices no hipergrafo é: ", HG.number_of_nodes())

    #L = hmod.last_step(HG, A = K, wdc=hmod.linear)
    #print(L)
    
    conjuntos_json = json.dumps([list(conjunto) for conjunto in L])

    with open('Resultados/Hipergrafo/Comunidades-HG.json', 'w') as f:
        f.write(conjuntos_json)
    
    print(f'{len(K)} comunidades detectadas no grafo com KUMAR!')

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

def plot_resultados(dicionario, title, color):
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
    plt.show()

def grafo_equivalente(grafo : nx.Graph, s : int):
    auxG = nx.Graph()

    for u, v, data in grafo.edges(data=True):
        if 'weight' in data and data['weight'] >= s:
            auxG.add_edge(u, v, weight=data['weight'])
    
    return auxG

def grafos_iguais(G1, G2):
    print(len(set(G1.nodes)))
    print(len(set(G2.nodes)))
    
    if set(G1.nodes) == set(G2.nodes) and set(G1.edges) == set(G2.edges):
        return True
    else:
        return False

def ordena(dicionario):
    return dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
