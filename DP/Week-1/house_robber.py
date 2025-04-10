#APPROACH - 1 (RECURSION)
# def house_robber(arr,idx):
#     if idx == 0:
#         return arr[idx]
#     if idx < 0:
#         return float('-inf')
#     pick =arr[idx] + house_robber(arr,idx-2)
#     not_pick = house_robber(arr,idx-1)
#     return max(pick,not_pick)
# arr = [2,1,4,9]
# n = len(arr)
# print(house_robber(arr,n-1))

#APPROACH - 2 (MEMOIZATION)
# def house_robber(arr,idx,dp):
#     if idx == 0:
#         return arr[idx]
#     if idx < 0:
#         return float('-inf')
#     if dp[idx] != -1:
#         return dp[idx]
#     pick =arr[idx] + house_robber(arr,idx-2,dp)
#     not_pick = house_robber(arr,idx-1,dp)
#     dp[idx] = max(pick,not_pick)
#     return dp[idx]
# arr = [2,1,4,9]
# n = len(arr)
# dp = [-1]*(n)
# print(house_robber(arr,n-1,dp))

#APPROACH - 3 (TABULATION)
# def house_robber(arr,dp,n):
#     for i in range(2,n):
#         dp[i] = max(arr[i]+dp[i-2],dp[-1])
#     return dp[n-1]
# arr = [1,2,3,1,3,5,8,1,9]
# n = len(arr)
# dp = [-1]*(n)
# dp[0] = arr[0]
# dp[1] = max(arr[0],arr[1])
# print(house_robber(arr,dp,n))

# The length of the array should minimum 2 for the above codes


# APPROACH - 4 (SPACE OPTIMIZATION)
def house_robber(arr,n):
    prev2 = arr[0]
    prev = max(arr[0],arr[1])
    for i in range(2,n):
        curr = max(arr[i]+prev2,prev)
        prev2 = prev
        prev = curr
    return prev


arr = [1,2,3,1,3,5,8,1,9]
n = len(arr)
print(house_robber(arr,n))