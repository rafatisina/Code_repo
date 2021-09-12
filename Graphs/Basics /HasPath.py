def HasPath_DFS(Graph, source, destination):
    #
    if source == destination:
        return True
    for nb in graph[source]:
        if HasPath_DFS(graph, nb, destination):
            return True
    return False

def HasPath_BFS(Graph, source, destination):
    # DFS
    queue = [source]

    while len(queue) > 0:
        current = queue.pop(0)
        if current == destination:
            return True
        for nb in graph[current]:
            queue.append(nb)
    return False



if __name__ == '__main__':
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'k': []
    }

res = HasPath_BFS(graph, 'g', 'k')
print(res)
