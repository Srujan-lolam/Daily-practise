# def longest_increasing_subsequence(arr):
#     n = len(arr)
#     dp = [-1 for _ in range(n)]
#     def helper_function(arr,idx,prev):
#         if idx == n:
#             return 0
#         pick = -1e9
#         if prev == -1 or arr[idx] > arr[prev]:
#             pick = 1 + helper_function(arr,idx+1,idx)
#         not_pick = helper_function(arr,idx+1,prev)
#         dp[idx] = max(pick,not_pick)
#         return dp[idx]
#     return helper_function(arr,0,-1)
# arr = [10,9,2,5,3,7,101,18]
# print(longest_increasing_subsequence(arr))

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n)] for _ in range(n+1)]
    def helper_function(idx, prev):
        if idx == n:
            return 0
        if dp[idx][prev+1] != -1:
            return dp[idx][prev+1]
        
        pick = 0
        if prev == -1 or arr[idx] > arr[prev]:
            pick = 1 + helper_function(idx+1, idx)
        not_pick = helper_function(idx+1, prev)
        
        dp[idx][prev+1] = max(pick, not_pick)
        return dp[idx][prev+1]
    
    return helper_function(0, -1)
arr = [10,9,2,5,3,7,101,18]
print(longest_increasing_subsequence(arr))