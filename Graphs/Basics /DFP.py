def DepthFirstPrint_it(Graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for nf in Graph[current]:
            stack.append(nf)


def DepthFirstPrint_rec(Graph, source):
    print(source)
    for nf in Graph[source]:
        DepthFirstPrint_rec(graph, nf)


if __name__ == '__main__':
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }

DepthFirstPrint_rec(graph, 'a')
