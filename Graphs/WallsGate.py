class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        GATE = 0
        EMPTY = 2147483647

        m = len(rooms)
        n = len(rooms[0])

        queue = deque([])

        for row in range(m):
            for col in range(n):
                if rooms[row][col] == GATE:
                    queue.append([row, col])

        while queue:
            point = queue.popleft()
            row, col = point

            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]

                if newRow < 0 or newCol < 0 or newRow >= m or newCol >= n or rooms[newRow][newCol] != EMPTY:
                    continue
                rooms[newRow][newCol] = rooms[row][col] + 1

                queue.append([newRow, newCol])

                 
