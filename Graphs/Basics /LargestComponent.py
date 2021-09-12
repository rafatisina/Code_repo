def exploreSize(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for nb in graph[node]:
        size += exploreSize(graph, nb, visited)
    return size


def LargestComponent(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size

    return longest


if __name__ == '__main__':
    res = LargestComponent({
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    })

    print(res)
