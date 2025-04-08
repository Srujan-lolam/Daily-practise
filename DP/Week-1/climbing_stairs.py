#APPROACH - 1 (RECURSION)
# def no_of_ways(n):
#     if n == 0 or n == 1:
#         return 1
#     return no_of_ways(n-1) + no_of_ways(n-2)
# n = 5
# print(no_of_ways(n))

#APPROACH - 2 (MEMOIZATION)
# def no_of_ways(n,dp):
#     if n == 0 or n == 1:
#         dp[n] = 1
#         return dp[n]
#     if dp[n] != -1:
#         return dp[n]
#     dp[n] = no_of_ways(n-1,dp) + no_of_ways(n-2,dp)
#     return dp[n]
# n = 5
# dp = [-1]*(n+1)
# print(no_of_ways(n,dp))

# APPROACH - 2 (MEMOIZATION)
# def no_of_ways(n,dp):
#     for i in range(2,n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
# n = 7
# dp = [-1]*(n+1)
# dp[0] = 1
# dp[1] = 1
# print(no_of_ways(n,dp))

# APPROACH - 2 (MEMOIZATION)
def no_of_ways(n):
    curr = 0
    step_one = 1
    step_two = 1
    for i in range(2,n+1):
        curr = step_two + step_one
        step_two = step_one
        step_one = curr
    return curr
n = 7
print(no_of_ways(n))

    
