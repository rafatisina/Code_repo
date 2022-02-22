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


# Capacity of the knapsack = W
# weight list : wt=[]
# price list : pr=[]
# No. of items = N



