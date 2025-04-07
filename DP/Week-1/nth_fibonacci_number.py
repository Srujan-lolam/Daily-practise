#APPROACH - 1 (RECURSION)
# def nth_fibonacci_number(n):
#     if n == 0 :
#         return 0
#     if n == 1:
#         return 1
#     return nth_fibonacci_number(n-1) + nth_fibonacci_number(n-2)
# n = 5
# dp = [0]*(n+1)
# print(nth_fibonacci_number(n))

# APPROACH - 2 (MEMOIZATION)
# def nth_fibonacci_number(n,dp):
#     if n == 0 :
#         return dp[0]
#     if n == 1:
#         return dp[1]
#     if dp[n] != -1:
#         return dp[n]
#     dp[n] = nth_fibonacci_number(n-1,dp) + nth_fibonacci_number(n-2,dp)
#     return dp[n]
# n = 6
# dp = [-1]*(n+1)
# dp[0] = 0
# dp[1] = 1
# print(nth_fibonacci_number(n,dp))

# APPROACH - 3 (Tabulation)
# def nth_fibonacci_number(n,dp):
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2,n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
# n = 6
# dp = [-1]*(n+1)
# print(nth_fibonacci_number(n,dp))

# APPROACH - 4 (SPACE OPTIMIZATION)
def nth_fibonacci_number(n,dp):
    first_prev = 1
    second_prev = 0
    current = 0
    for i in range(2,n+1):
        current = first_prev + second_prev
        second_prev = first_prev
        first_prev = current
    return current
n = 5
dp = [-1]*(n+1)
print(nth_fibonacci_number(n,dp))

