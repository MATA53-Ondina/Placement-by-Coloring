def colorGraph(graph, k):

    coloring = {}

    for cont in k: # Percorre a lista com os vertices ordenados

        color = 1
        auxiliar = set([coloring.get(i) for i in graph.adj[cont]]) # Percorre a lista de adjacentes do grafo e atribui a variavel auxiliar

        for c in auxiliar: # Percorre a lista de auxiliar, que é a lista de cores dos vertices adjacentes
            if color != c:
                break
            else:
                color = color + 1

        coloring[cont] = color
    return coloring
