def BreadFirstPrint(Graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for nf in Graph[current]:
            queue.append(nf)


if __name__ == '__main__':
    graph = {
        'a': ['c', 'b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }

BreadFirstPrint(graph, 'a')
