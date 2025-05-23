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

#APPROACH - 3

def minimum_coins(arr,dp,n,target):
    for i in range(target + 1):
        if i % arr[0] == 0:
            dp[0][i] = i // arr[0]
        else:
            dp[0][i] = int(1e9)
    for i in range(1,n):
        for target in range(1,target+1):
            not_pick = dp[i-1][target]
            pick = int(1e9)  
            if arr[i] <= target:
                pick = 1 + dp[i][target - arr[i]]
            dp[i][target] = min(not_pick,pick)
    ans = dp[n-1][target]
    if ans >= 1e9:
        return -1
    return ans
    

arr = [1,2,3]
n = len(arr)
target = 7
dp = [[1e9 for _ in range(target + 1)] for _ in range(n)]
print(minimum_coins(arr,dp,n,target))
