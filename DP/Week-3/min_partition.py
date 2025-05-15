def minimum_absolute_diff(arr,dp,totSum):
    n = len(arr)
    for i in range(n):
        for target in range(totSum+1):
            if i == 0:
                dp[i][0] = True 
            if arr[0] <= totSum:
                dp[0][arr[0]] = True
            pick = False
            if arr[i] <= target:
                pick = dp[i-1][target - arr[i]]
            not_pick = dp[i-1][target]
            dp[i][target] = pick or not_pick
    ans = 1e9
    for i in range(totSum+1):
        if dp[n-1][i]:
            s1 = i 
            s2 = totSum - i 
            diff = abs(s1-s2)
            ans = min(ans ,diff)
    return ans
arr = [1,2,3,4]
totSum = sum(arr)
n = len(arr)
dp = [[False for _ in range(totSum+1)] for _ in range(n)]
print(minimum_absolute_diff(arr,dp,totSum))


# there are minor issues with above code , try finding them when you are revising them
#below is the fixed version
def minimum_absolute_diff(arr, dp, totSum):
    n = len(arr)
    
    # Base cases
    for i in range(n):
        dp[i][0] = True  # Zero sum is always possible

    if arr[0] <= totSum:
        dp[0][arr[0]] = True

    # DP fill
    for i in range(1, n):
        for target in range(totSum + 1):
            pick = dp[i-1][target - arr[i]] if arr[i] <= target else False
            not_pick = dp[i-1][target]
            dp[i][target] = pick or not_pick

    # Find minimum absolute difference
    ans = float('inf')
    for s1 in range(totSum + 1):
        if dp[n-1][s1]:
            s2 = totSum - s1
            ans = min(ans, abs(s1 - s2))
    
    return ans

# Test
arr = [1, 2, 3, 4]
totSum = sum(arr)
n = len(arr)
dp = [[False for _ in range(totSum + 1)] for _ in range(n)]
print(minimum_absolute_diff(arr, dp, totSum))
