#APPROACH - 1 (RECURSION)
# def lcs(s1,s2,idx1,idx2,n1,n2):
#     if idx1 < 0 or idx2 < 0:
#         return 0
#     if s1[idx1] == s2[idx2]:
#         return 1 + lcs(s1,s2,idx1-1,idx2-1,n1,n2)
#     else:
#         return max(lcs(s1,s2,idx1-1,idx2,n1,n2),lcs(s1,s2,idx1,idx2-1,n1,n2))

# s1 = "xypod"
# s2 = "dcadb"
# n1 = len(s1)
# n2 = len(s2)
# print(lcs(s1,s2,n1-1,n2-1,n1,n2))

#APPROACH - 2 (MEMOIZATION)
# def lcs(s1,s2,idx1,idx2,n1,n2,dp):
#     if idx1 < 0 or idx2 < 0:
#         return 0
#     if dp[idx1][idx2] != 0:
#         return dp[idx1][idx2]
#     if s1[idx1] == s2[idx2]:
#         dp[idx1][idx2] = 1 + lcs(s1,s2,idx1-1,idx2-1,n1,n2,dp)
#     else:
#         dp[idx1][idx2] = max(lcs(s1,s2,idx1-1,idx2,n1,n2,dp),lcs(s1,s2,idx1,idx2-1,n1,n2,dp))
#     return dp[idx1][idx2]

# s1 = "od"
# s2 = "db"
# n1 = len(s1)
# n2 = len(s2)
# dp = [[0 for _ in range(n2)] for _ in range(n1)]
# print(lcs(s1,s2,n1-1,n2-1,n1,n2,dp))

#APPROACH - 3 (TABULATION)
def lcs(s1,s2,dp):
    n1 = len(s1)
    n2 = len(s2)
    dp[0][0] = 1 if s1[0] == s2[0] else 0
    for i in range(1,n1):
        if s1[i] == s2[0]:
            dp[i][0] = 1 
        else : 
            dp[i][0] = dp[i-1][0]
    for j in range(1,n2):
        if s2[j] == s1[0]:
            dp[0][j] = 1 
        else:
            dp[0][j] = dp[0][j-1]
    for x in range(1,n1):
        for y in range(1,n2):
            if s1[x] == s2[y]:
                dp[x][y] = 1 + dp[x-1][y-1]
            else:
                dp[x][y] = max(dp[x-1][y],dp[x][y-1])
    return dp[n1-1][n2-1]
s1 = "hsjnpq"
s2 = "spdbcsudycbsdjhcbsdjchbq"
n1 = len(s1)
n2 = len(s2)
dp = [[0 for _ in range(n2)] for _ in range(n1)]
print(lcs(s1,s2,dp))