#APPROACH - 1 - (RECURSION)
# def minimum_pathSum(triangle,row_idx,col_idx,m):
#     if row_idx == m-1 :
#         return triangle[row_idx][col_idx]
#     n = len(triangle[row_idx])
#     return triangle[row_idx][col_idx] + min(minimum_pathSum(triangle,row_idx+1,col_idx,m),minimum_pathSum(triangle,row_idx+1,col_idx+1,m))
    
# triangle = [[1], [100, 3], [3, 6, 7], [8, 9, 6, 10]]
# print(minimum_pathSum(triangle,0,0,len(triangle)))


#APPROACH - 2 (MEMOIZATION)
# def minimum_pathSum(triangle,row_idx,col_idx,m,dp):
#     if row_idx == m-1 :
#         dp[row_idx][col_idx] = triangle[row_idx][col_idx]
#         return dp[row_idx][col_idx]
#     if dp[row_idx][col_idx] != -1:
#         return dp[row_idx][col_idx]
#     n = len(triangle[row_idx])
#     dp[row_idx][col_idx]= triangle[row_idx][col_idx] + min(minimum_pathSum(triangle,row_idx+1,col_idx,m,dp),minimum_pathSum(triangle,row_idx+1,col_idx+1,m,dp))
#     return dp[row_idx][col_idx]
# triangle = [[1], [100, 3], [3, 6, 7], [8, 9, 6, 10]]
# dp = []
# for i in range(len(triangle)):
#     n = len(triangle[i])
#     dp.append([-1]*n)
# print(minimum_pathSum(triangle,0,0,len(triangle),dp))


#APPROACH - 3 (TABULATION)
# def minimum_pathSum(triangle,dp):
#     m = len(triangle)
#     for i in range(m):
#         n = len(triangle[i])
#         for j in range(n):
#             if i == 0 and j == 0:
#                 dp[i][j] = triangle[0][0]
#             else:
#                 up = 1e9
#                 right = 1e9
#                 if i > 0:
#                     if j != n-1:
#                         up = dp[i-1][j]
#                 if j > 0:
#                     right = dp[i-1][j-1]
#                 dp[i][j] = triangle[i][j] + min(up,right)
#     return min(dp[m-1])

    
# triangle = [[1], [2, 0], [3, 6, 7], [8, 9, 6, 10]]
# dp = []
# for i in range(len(triangle)):
#     n = len(triangle[i])
#     dp.append([0]*n)
# print(minimum_pathSum(triangle,dp))

#APPROACH - 4 (SPACE OPTIMIZATION)
def minimum_pathSum(triangle,dp):
    m = len(triangle)
    dp[0] = triangle[0][0]
    for i in range(m):
        n = len(triangle[i])
        curr = [0]*(n)
        for j in range(n):
            if i == 0 and j == 0:
                curr[j] = dp[j]
            else:
                up = 1e9
                right = 1e9
                if i > 0:
                    if j != n-1:
                        up = dp[j]
                if j > 0:
                    right = dp[j-1]
                curr[j] = triangle[i][j] + min(up,right)
        dp = curr
    return min(dp)    
triangle = [[1], [2, 0], [3, 6, 7], [8, 9, 6, 10]]
dp = [0]
print(minimum_pathSum(triangle,dp))