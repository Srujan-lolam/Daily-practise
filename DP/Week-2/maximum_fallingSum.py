#APPROACH - 1 (RECURSION)
# def maximum_pathSum(matrix,n,m,row_idx,col_idx):
#     if col_idx < 0 or col_idx >= m:
#         return -1e9
#     if row_idx == n :
#         return matrix[row_idx][col_idx]
#     return matrix[row_idx][col_idx] + max(maximum_pathSum(matrix,n,m,row_idx+1,col_idx-1),maximum_pathSum(matrix,n,m,row_idx+1,col_idx+1),maximum_pathSum(matrix,n,m,row_idx+1,col_idx))

# matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
# n = len(matrix)
# m = len(matrix[0])
# max1 = -1e9
# for i in range(m):
#     ans = maximum_pathSum(matrix,n-1,m,0,i)
#     max1 = max(max1,ans)
# print(max1)


#APPROACH - 2 (MEMOIZATION)
# def maximum_pathSum(matrix,n,m,row_idx,col_idx,dp):
#     if col_idx < 0 or col_idx >= m:
#         return -1e9
#     if row_idx == n :
#         return matrix[row_idx][col_idx]
#     if dp[row_idx][col_idx] != -1:
#         return dp[row_idx][col_idx]
#     dp[row_idx][col_idx] = matrix[row_idx][col_idx] + max(maximum_pathSum(matrix,n,m,row_idx+1,col_idx-1,dp),maximum_pathSum(matrix,n,m,row_idx+1,col_idx+1,dp),maximum_pathSum(matrix,n,m,row_idx+1,col_idx,dp))
#     return dp[row_idx][col_idx]
# matrix = [[1, 2, 10, 4], [100, 3, 200, 1], [1, 1, 20, 2], [400, 2, 2, 1]]
# n = len(matrix)
# m = len(matrix[0])
# dp = [[-1 for i in range(m)] for j in range(n)]
# max1 = -1e9
# for i in range(m):
#     ans = maximum_pathSum(matrix,n-1,m,0,i,dp)
#     max1 = max(max1,ans)
# print(max1)


#APPROACH - 3 (TABULATION)
# def maximum_pathSum(matrix,n,m,dp):
#     for i in range(n):
#         for j in range(m):
#             if i == 0 :
#                 dp[i][j] = matrix[i][j]
#             else:
#                 left = -1e9
#                 right = -1e9
#                 up = dp[i-1][j]
#                 if j > 0:
#                     left = dp[i-1][j-1]
#                 if j+1 < m:
#                     right = dp[i-1][j+1]
#                 dp[i][j] = matrix[i][j] + max(up,left,right)
#     return max(dp[n-1])
# matrix = [[1, 2, 10, 4], [100, 3, 200, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
# n = len(matrix)
# m = len(matrix[0])
# dp = [[-1 for i in range(m)] for j in range(n)]
# max1 = -1e9
# print(maximum_pathSum(matrix,n,m,dp))


#APPROACH - 4 (SPACE OPTIMIZATION)
def maximum_pathSum(matrix,n,m,prev):
    for i in range(n):
        curr = [0]*(n)
        for j in range(m):
            if i == 0 :
                curr[j] = matrix[i][j]
            else:
                left = -1e9
                right = -1e9
                up = prev[j]
                if j > 0:
                    left = prev[j-1]
                if j+1 < m:
                    right = prev[j+1]
                curr[j] = matrix[i][j] + max(up,left,right)
        prev = curr
    return max(prev)
matrix = [[1, 2, 10, 4], [100, 3, 200, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
n = len(matrix)
m = len(matrix[0])
prev = [0 for i in range(m)]
max1 = -1e9
print(maximum_pathSum(matrix,n,m,prev))