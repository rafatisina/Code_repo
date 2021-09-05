class Solution:

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        d={}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i+j not in d:
                    d[i+j] =[matrix[i][j]]
                else:
                    d[i+j].append(matrix[i][j])

        res=[]
        for k in d.items():
            if k[0] % 2==0:
                [res.append(x) for x in k[1][::-1]]
            else:
                [res.append(x) for x in k[1]]
        return res

           
