def BuildGraph(edges):
    G = {}
    for e in edges:
        [a, b] = e
        if a not in G:
            G[a] = []
        if b not in G:
            G[b] = []
        G[a].append(b)
        G[b].append(a)
    return G


def HasPath_DFS(graph, source, destination, visited):
    if source == destination:
        return True
    if source in visited:
        return False
    visited.add(source)
    for nb in graph[source]:
        if HasPath_DFS(graph, nb, destination, visited):
            return True
    return False


def UnidirectedPath(edges, nodeA, nodeB):
    Graph_generated = BuildGraph(edges)
    visited = set()
    return HasPath_DFS(Graph_generated, nodeA, nodeB, visited)


if __name__ == '__main__':
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['k', 'j'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]
    res = UnidirectedPath(edges, 'i', 'j')
    print(res)
