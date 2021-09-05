class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        columns=len(matrix[0])
        up=0
        left=0
        down=rows-1
        right=columns-1
        results=[]

        while len(results) < rows*columns:
            for col in range(left, right+1):
                results.append(matrix[up][col])
            for row in range(up+1,down+1):
                results.append(matrix[row][right])
            if up != down:
                for col in range(right-1,left-1,-1):
                    results.append(matrix[down][col])
            if left != right:
                for row in range(down-1,up,-1):
                    results.append(matrix[row][left])
            left+=1
            right-=1
            up+=1
            down-=1
        return results  
