# This is similar to subsetSum , just add a for loop for the tabulation method and count dp[i][target == true] ,count += 1,return count,else below
# approaches are also fyn 
# def countsubsetSum(arr,target,idx,dp):
#     if target == 0:
#         return 1
#     if idx == 0:
#         return (arr[idx] == target)
#     if dp[idx][target] != -1:
#         return dp[idx][target]
#     not_pick = countsubsetSum(arr,target,idx-1,dp)
#     pick = 0
#     if arr[idx] <= target:
#         pick = countsubsetSum(arr,target-arr[idx],idx-1,dp)
#     dp[idx][target] = pick + not_pick
#     return dp[idx][target]

# arr = [1,2,2,3]
# target = 3
# n = len(arr)
# dp = [[-1 for _ in range(target+1)] for _ in range(n)]
# print(countsubsetSum(arr,target,n-1,dp))

def countSubsetSumK(arr,dp,n,target):
    for i in range(n):
        dp[i][0] = 1
    if arr[0] <= target:
        dp[0][arr[0]] = 1
    for i in range(1,n):
        for tar in range(1,target+1):
            not_pick = dp[i-1][tar]
            pick = 0
            if arr[i] <= tar:
                pick += dp[i-1][tar - arr[i]]
            dp[i][tar] = pick + not_pick
    return dp[n-1][target]

arr = [1,2,2,3]
target = 3
n = len(arr)
dp = [[0 for _ in range(target+1)] for _ in range(n)]
print(countSubsetSumK(arr,dp,n,target))


