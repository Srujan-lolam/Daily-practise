# APPROACH - 1 (RECURSION)
# def minimum_coins(arr,idx,target):
#     if idx == 0:
#         if target%arr[idx] == 0:
#             return target//arr[idx]
#         else:
#             return 1e9
#     if target == 0:
#         return 0
#     pick = 1e9
#     if arr[idx] <= target:
#         pick = 1 + minimum_coins(arr,idx,target-arr[idx])
#     not_pick = minimum_coins(arr,idx-1,target)
#     return min(pick , not_pick)

# arr = [1,2,3]
# n = len(arr)
# target = 7
# print(minimum_coins(arr,n-1,target))

#APPROACH - 2 (MEMOIZATION)
# def minimum_coins(arr,idx,target,dp):
#     if idx == 0:
#         if target%arr[idx] == 0:
#             return target//arr[idx]
#         else:
#             return 1e9
#     if target == 0:
#         return 0
#     if dp[idx][target] != -1:
#         return dp[idx][target]
#     pick = 1e9
#     if arr[idx] <= target:
#         pick = 1 + minimum_coins(arr,idx,target-arr[idx],dp)
#     not_pick = minimum_coins(arr,idx-1,target,dp)
#     dp[idx][target] = min(pick , not_pick)
#     print(dp)
#     return dp[idx][target]

# arr = [1,2,3]
# n = len(arr)
# target = 7
# dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
# print(minimum_coins(arr,n-1,target,dp))