#APPROACH - 1 (RECURSION)
# def unique_paths(m,n):
#     if m == 0 and n == 0:
#         return 1
#     if m < 0 or n < 0:
#         return 0
#     return unique_paths(m-1,n) + unique_paths(m,n-1)
# m = 3
# n = 2 
# print(unique_paths(m-1,n-1))

# APPROACH - 2 (MEMOIZATION)
# def unique_paths(m,n,dp):
#     if m == 0 and n == 0:
#         return 1
#     if m < 0 or n < 0:
#         return 0
#     if dp[m][n] != -1:
#         return dp[m][n]
#     dp[m][n] = unique_paths(m-1,n,dp) + unique_paths(m,n-1,dp)
#     return dp[m][n]
# m = 3
# n = 2 
# dp = [[-1 for i in range(n)] for i in range(m)]
# print(unique_paths(m-1,n-1,dp))

# So your intuition is right in thinking “there are extra calls,”
# but in Big-O, we only care about unique computed subproblems → hence O(m × n).


# APPROACH - 3 (TABULATION)
# def unique_paths(m,n,dp):
#     for i in range(m):
#         for j in range(n):
#             if i == 0 or j == 0:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     return dp[m-1][n-1]
    
# m = 4
# n = 4
# dp = [[0 for i in range(n)] for i in range(m)]
# print(unique_paths(m,n,dp))

# APPROACH-4 (SPACE OPTIMIZATION)
def unique_paths(m,n):
    row = [1 for i in range(m)]
    for i in range(m):
        curr = [0 for i  in range(n)]
        for j in range(n):
            if i == 0 or j == 0:
                curr[j] = 1
            else:
                curr[j] += row[i-1] + curr[j-1]
        row = curr
    return curr[n-1]
    
m = 3
n = 2

print(unique_paths(m,n))