# APPROACH - 1(RECURSION)
# def minimum_path_sum(grid,m,n):
#     if m == 0 and n == 0:
#         return grid[0][0]
#     if m < 0 or n < 0:
#         return 1e9
#     return grid[m][n] + min(minimum_path_sum(grid,m-1,n),minimum_path_sum(grid,m,n-1))

# grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
# m = len(grid)
# n = len(grid[0])
# print(minimum_path_sum(grid,m-1,n-1))

# APPROACH - 2 (MEMOIZATION)
# def minimum_path_sum(grid,m,n,dp):
#     if m == 0 and n == 0:
#         return grid[0][0]
#     if m < 0 or n < 0:
#         return 1e9
#     if dp[m][n] != -1:
#         return dp[m][n]
#     dp[m][n] = grid[m][n] + min(minimum_path_sum(grid,m-1,n,dp),minimum_path_sum(grid,m,n-1,dp))
#     return dp[m][n]
# grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
# m = len(grid)
# n = len(grid[0])
# dp = [[-1 for i in range(n)] for i in range(m)]
# print(minimum_path_sum(grid,m-1,n-1,dp))

    
# APPROACH - 3 (TABULATION)
# def minimum_path_sum(grid,m,n,dp):
#     for i in range(m):
#         for j in range(n):
#             if i == 0 and j == 0:
#                 dp[0][0] = grid[0][0]
#             else:
#                 if i != 0 and j != 0:
#                     dp[i][j] = grid[i][j] + min(dp[i][j-1],dp[i-1][j])
#                 elif i == 0 and j != 0:
#                     dp[i][j] = grid[i][j] + dp[i][j-1]
#                 else:
#                     dp[i][j] =grid[i][j] + dp[i-1][j]
#     return dp[m-1][n-1]

# grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
# m = len(grid)
# n = len(grid[0])
# dp = [[0 for i in range(n)] for i in range(m)]
# print(minimum_path_sum(grid,m,n,dp))
# In the approach 3 ,code is fyn but we can still refactor by reducing the number of lines like below

# def minimum_path_sum(grid,m,n,dp):
#     for i in range(m):
#         for j in range(n):
#             if i == 0 and j == 0:
#                 dp[0][0] = grid[0][0]
#             else:
#                 up = 1e9
#                 left = 1e9
#                 if i > 0:
#                     up = dp[i-1][j]
#                 if j > 0:
#                     left = dp[i][j-1]
#                 dp[i][j] += grid[i][j] + min(up,left)
#     return dp[m-1][n-1]

# grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
# m = len(grid)
# n = len(grid[0])
# dp = [[0 for i in range(n)] for i in range(m)]
# print(minimum_path_sum(grid,m,n,dp))


#APPROACH - 5 (SPACE OPTMIZATION)
def minimum_path_sum(grid,m,n,dp):
    for i in range(m):
        prev = [0]*(n)
        for j in range(n):
            if i == 0 and j == 0:
                prev[j] = grid[i][j]
            else:
                up = 1e9
                left = 1e9
                if i > 0:
                    up = dp[j]
                if j > 0:
                    left = prev[j-1]
                prev[j] += grid[i][j] + min(up,left)
        dp = prev
    return prev[n-1]
grid = [[1,3,1],[1,5,1],[4,2,1]]
# grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
m = len(grid)
n = len(grid[0])
dp = [0]*(n)
print(minimum_path_sum(grid,m,n,dp))