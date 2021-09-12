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


def ShortestPath(edges, nodeA, nodeB):
    Graph = BuildGraph(edges)
    queue = [[nodeA, 0]]
    visited = set()
    visited.add(nodeA)

    while len(queue) > 0:
        [node, Distance] = queue.pop(0)
        if node == nodeB:
            return Distance
        for nb in Graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append([nb, Distance + 1])

    return -1


if __name__ == '__main__':
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]

print(ShortestPath(edges, 'w', 'z'))
