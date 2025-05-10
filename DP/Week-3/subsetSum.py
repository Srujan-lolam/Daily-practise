#APPROACH - 1 (RECURSION)
# def subsetSum(arr,idx,sum1,k):
#     if idx < 0:
#         return sum1 == k 
#     pick = subsetSum(arr,idx-1,sum1+arr[idx],k)
#     not_pick = subsetSum(arr,idx-1,sum1,k)
#     return pick or not_pick 
# arr = [0,0,0]
# n = len(arr)
# target = 0
# print(subsetSum(arr,n-1,0,target))


#APPROACH - 2 (MEMOIZATION)
# def subsetSum(arr,idx,target,dp):
#     if idx == 0:
#         return arr[0] == target 
#     if target == 0:
#         return True 
#     if dp[idx][target] != -1:
#         return dp[idx][target]
#     pick = subsetSum(arr,idx-1,target-arr[idx],dp)
#     not_pick = subsetSum(arr,idx-1,target,dp)
#     dp[idx][target] = pick or not_pick 
#     return dp[idx][target]
# arr = [2,1]
# n = len(arr)
# target = 2
# dp = [[-1 for i in range(target+1)] for i in range(n)]
# print(dp)
# print(subsetSum(arr,n-1,target,dp))


# APPROACH - 3 (TABULATION)
# def subsetSum(arr,target,dp):
#     n = len(arr)
#     for i in range(target+1):
#         dp[0][i] = False
#     for i in range(n):
#         dp[i][0] = True
#     for i in range(1,n):
#         for j in range(1,target+1):
#             if i == 0:
#                 dp[i][j] = False
#             if j == 0:
#                 dp[i][j] = True 
#             pick = False
#             if arr[i] <= j:
#                 pick = dp[i-1][j-arr[i]]
#             not_pick = dp[i-1][j]
#             dp[i][j] = pick or not_pick
#     return dp[n-1][target]
    
# arr = []
# n = len(arr)
# target = 1
# dp = [[None for i in range(target+1)] for i in range(n)]
# print(subsetSum(arr,target,dp))

# not sure of the tabulation approach 
