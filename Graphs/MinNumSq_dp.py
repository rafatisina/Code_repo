class Solution(object):
    def numSquares(self, n):
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        dp=[float('inf')]*(n+1)
        dp[0]=0

        for i in range(n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min (dp[i], dp[i-square]+1)
        return dp[-1]        
