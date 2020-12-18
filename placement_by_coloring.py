#!/usr/bin/env python3
# Global
colorVertices = []
gama = [(2, 0), (4, 1), (2, 2), (5, 3), (6, 4), (1, 5), (5, 6), (3, 7)] # tuples: (popularidade, file)


class Graph:
 
    # Constructor
    def __init__(self, edges, N):
 
        self.adj = [[] for _ in range(N)]
        self.arq = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)
 
 
def OrdenaVerticesDescrescente(G):
    A = []
    K = []
    for u in G:
        A.append((len(u.adj), u))
    sorted(A, reverse = True)
    for (_,v) in A:
        K.append(v)
    return K


def OrdenaArquivos(gama):
    sorted(gama, reverse = True)
    return gama



def GreedyColoring(graph, K):
    global colorVertices
    result = {}
 
    for u in K:
        color = 1
        assigned = set([result.get(i) for i in graph.adj[u]])
        for c in assigned:
            if color != c:
                break
            else:
                color = color + 1
        result[u] = color

    for j in range(len(K)):
        colorVertices[j] = 0

    for v in range(len(K)):
        colorVertices[v] = colors[result[v]]


# Largest-First
def LargestFirst(graph):
    K = OrdenaVerticesDescrescente(graph)
    GreedyColoring(graph, K)


def PlacementByColoring(graph, gama):
    global colorVertices
    lambd = 50
    teta = 0

    LargestFirst(graph) # O(|V|+|E|)
    delta = OrdenaArquivos(gama)
    for v in graph: # O(|V|*50)
        for i in range(lambd):
            teta = colorVertices[v]
            v.arq = delta[(teta * lambd) + i]


if __name__ == '__main__':
    colors = [-1, 0, 1, 2, 3]

    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
    N = 6
    graph = Graph(edges, N)
 
    PlacementByColoring(graph, gama)