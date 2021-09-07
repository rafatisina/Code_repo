class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        import numpy as np
        res=[]
        for k in range(numRows):
            void = np.ones(k+1,dtype=int)
            res.append(void)
            if k>1:
                for j in range(1,len(res[k])-1):
                    res[k][j]=(res[k-1][j-1]+res[k-1][j])
        return res
