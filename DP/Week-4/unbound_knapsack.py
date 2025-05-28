#APPROACH - 1 (RECURSION) -
# constraints - all the wieghts should be non zero 

# def unbound(wt,val,W,idx):
#     if idx < 0 or W == 0:
#         return 0
#     not_pick = unbound(wt,val,W,idx-1)
#     pick = -1e9
#     if wt[idx] <= W and idx >= 0:
#         pick = val[idx] + unbound(wt,val,W-wt[idx],idx)
#     return max(not_pick,pick)

# wt = [2, 4, 6]
# val = [5, 11, 13]
# W = 10
# n = len(wt)
# print(unbound(wt,val,W,n-1))

#APPROACH - 2 (MEMOIZATION)

# def unbound(wt,val,W,idx,dp):
#     if idx < 0 or W == 0:
#         return 0
#     if dp[idx][W] != -1:
#         return dp[idx][W]
#     not_pick = unbound(wt,val,W,idx-1,dp)
#     pick = -1e9
#     if wt[idx] <= W and idx >= 0:
#         pick = val[idx] + unbound(wt,val,W-wt[idx],idx,dp)
#     dp[idx][W] =  max(not_pick,pick)
#     return dp[idx][W]

# wt = [11]
# val = [100]
# W = 10
# n = len(wt)
# dp = [[-1 for _ in range(W+1)] for _ in range(n)]
# print(unbound(wt,val,W,n-1,dp))

#APPROACH - 3 (TABULATION)
def unbound(wt,val,W,dp,n):
    try:
        for weight in range(W+1):
            if weight%wt[0] == 0:
                dp[0][weight] = (weight//wt[0])*val[0]
        for i in range(1,n):
            for j in range(1,W+1):
                not_pick = dp[i-1][j]
                pick = 0
                if wt[i] <= j:
                    pick =val[i] + dp[i][j-wt[i]]
                dp[i][j] = max(pick,not_pick)
        print(dp)
        return dp[n-1][W]
    except Exception as e :
        print("Exception caught = ",e)


wt = [0, 4, 6]
val = [5, 11, 13]
W = 10
n = len(wt)
dp = [[0 for _ in range(W+1)] for _ in range(n)]
print(unbound(wt,val,W,dp,n))