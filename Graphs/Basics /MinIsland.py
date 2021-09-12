def MinIsland(Grid):
    visited = set()
    minsize = 100000
    for r in range(len(Grid)):
        for c in range(len(Grid[0])):
            size = exploreSize(Grid, r, c, visited)
            if (size < minsize) and (size > 0):
                minsize = size
    return minsize


def exploreSize(Grid, r, c, visited):
    rowinbounds = (0 <= r) and (r < len(Grid))
    colinbounds = (0 <= c) and (c < len(Grid[0]))

    if not rowinbounds or not colinbounds:
        return 0
    if Grid[r][c] == 'W':
        return 0
    pos = str(r) + ',' + str(c)
    if pos in visited:
        return 0
    visited.add(pos)
    size = 1
    size += exploreSize(Grid, r - 1, c, visited)
    size += exploreSize(Grid, r + 1, c, visited)
    size += exploreSize(Grid, r, c - 1, visited)
    size += exploreSize(Grid, r, c + 1, visited)

    return size


if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'L', 'W', 'W']
    ]
print(MinIsland(grid))
