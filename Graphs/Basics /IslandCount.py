def IslandCount(Grid):
    visited = set()
    count = 0
    for r in range(len(Grid)):
        for c in range(len(Grid[0])):
            if explore(Grid, r, c, visited):
                count += 1
    return count

def explore(Grid, r, c, visited):
    rowinbounds = (0 <= r) and (r < len(Grid))
    colinbounds = (0 <= c) and (c < len(Grid[0]))

    if not rowinbounds or not colinbounds:
        return False
    if Grid[r][c] == 'W':
        return False
    pos = str(r) + ',' + str(c)
    if pos in visited:
        return False
    visited.add(pos)
    explore(Grid, r - 1, c, visited)
    explore(Grid, r + 1, c, visited)
    explore(Grid, r, c - 1, visited)
    explore(Grid, r, c + 1, visited)

    return True


if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']
    ]
print(IslandCount(grid))
