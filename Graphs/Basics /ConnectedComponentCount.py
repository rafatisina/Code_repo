def explore(graph, node, visited):
    if node in visited:
        return False
    visited.add(node)
    for nb in graph[node]:
        explore(graph, nb, visited)

    return True


def ConnectedComponentCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count


if __name__ == '__main__':
    res =ConnectedComponentCount({
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2,4],
        4: [3,2]
    })

    print(res)
