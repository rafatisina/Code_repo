#capacity W
# weights and profirs for N items provided 

# Idea:  make a table dp[][] and consider all poosible weights
#  from 1 to w as columns and weights that we can choose as rows
# the state/cell dp[i][j] represents maximum attainable profit 
# if "j" is the capacity of the knapsack and the first "i" elements
# are included in in the weight/item array. 
# Hence the last cell represents the the answer state. 
# items can be included only if their weights are less than the
#capacity of the of the knapsack 

# note that the there are two possibilities for the condition
# where we can fill all columns which have weight > wt[i-1]

# Note that the running time complexity is O(N*W)
# Capacity of the knapsack = W
# weight list : wt=[]
# price list : pr=[]
# No. of items = N
def kProfit(W,N,wt,pr,dp):
    # Base Condition
    if N==0 or W==0:
        return 0
    if dp[N][W] is not None:
        return dp[N][W]
    if wt[N-1] <= W:
        dp[N][W] = max(pr[N-1]+kProfit(W-wt[N-1],N-1,wt,pr,dp), kProfit(W,N-1,wt,pr,dp))
        return dp[N][W]
    else:
        dp[N][W] = kProfit(W,N-1,wt,pr,dp)
        return dp[N][W]
if __name__ == '__main__':
    W = 11
    wt = [1, 2, 5, 6, 7]
    pr = [1, 6, 18, 22, 28]
    N = len(pr)
    # define DP array
    dp = [[None] * (W + 1) for _ in range(N + 1)]
    # Call for kProfit to calculate max profit
    maxProfit = kProfit(W,N,wt,pr,dp)
    print('Maximum Profit is : ',maxProfit)
