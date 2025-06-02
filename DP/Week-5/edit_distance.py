# APPROACH - 1 (RECURSION)
# def edit_distance(s1,s2,idx1,idx2):
#     if idx1 < 0:
#         return idx2 + 1
#     if idx2 < 0:
#         return idx1+1
#     if s1[idx1] == s2[idx2]:
#         return edit_distance(s1,s2,idx1-1,idx2-1)
#     insertion = edit_distance(s1,s2,idx1,idx2-1)
#     replace =edit_distance(s1,s2,idx1-1,idx2-1)
#     deletion =edit_distance(s1,s2,idx1-1,idx2)
#     return 1 + min(insertion,replace,deletion)

# s1 = "intention"
# s2 = "execution"
# m = len(s1)
# n = len(s2)
# print(edit_distance(s1,s2,m-1,n-1))


##APPROACH - 2 (MEMOIZATION)
# def edit_distance(s1,s2,idx1,idx2,dp):
#     if idx1 < 0:
#         return idx2 + 1
#     if idx2 < 0:
#         return idx1+1
#     if dp[idx1][idx2] != -1:
#         return dp[idx1][idx2]
#     if s1[idx1] == s2[idx2]:
#         dp[idx1][idx2] =  edit_distance(s1,s2,idx1-1,idx2-1,dp)
#         return dp[idx1][idx2]
#     insertion = edit_distance(s1,s2,idx1,idx2-1,dp)
#     replace =edit_distance(s1,s2,idx1-1,idx2-1,dp)
#     deletion =edit_distance(s1,s2,idx1-1,idx2,dp)
#     dp[idx1][idx2] = 1 + min(insertion,replace,deletion)
#     return dp[idx1][idx2]

# s1 = "intention"
# s2 = "execution"
# m = len(s1)
# n = len(s2)
# dp = [[-1 for _ in range(n)] for _ in range(m)]
# print(edit_distance(s1,s2,m-1,n-1,dp))

def edit_distance(s1,s2,dp,m,n):
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for row in range(1,m+1):
        for col in range(1,n+1):
            if s1[row-1] == s2[col-1]:
                dp[row][col] = dp[row-1][col-1]
            else:
                dp[row][col] = 1 + min(dp[row-1][col-1],dp[row-1][col],dp[row][col-1])
    return dp[m][n]

s1 = "intention"
s2 = "execution"
m = len(s1)
n = len(s2)
dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
print(edit_distance(s1,s2,dp,m,n))