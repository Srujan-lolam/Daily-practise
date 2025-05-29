# def lcs(s1,s2,count,idx1,idx2):
#     if idx1 == 0 or idx2 == 0:
#         return count
#     if s1[idx1] == s2[idx2]:
#         return lcs(s1,s2,count+1,idx1-1,idx2-1)
#     else:
#         return max(count,lcs(s1,s2,0,idx1-1,idx2),lcs(s1,s2,0,idx1,idx2-1))
# s1 = "abssdcpqru"
# s2 = "sjdgvgvvpqru"
# m = len(s1)
# n = len(s2)
# print(lcs(s1,s2,0,m-1,n-1))

# def lcs(s1,s2,count,idx1,idx2,dp):
#     if idx1 == 0 or idx2 == 0:
#         return count
#     if dp[idx1][idx2] != -1:
#         return dp[idx1][idx2]
#     if s1[idx1] == s2[idx2]:
#         dp[idx1][idx2] = lcs(s1,s2,count+1,idx1-1,idx2-1,dp)
#         return dp[idx1][idx2]
#     else:
#         dp[idx1][idx2] = max(count,lcs(s1,s2,0,idx1-1,idx2,dp),lcs(s1,s2,0,idx1,idx2-1,dp))
#         return dp[idx1][idx2]
# s1 = "abssdcpqru"
# s2 = "sjdgvgvvpqru"
# m = len(s1)
# n = len(s2)
# dp = [[-1 for _ in range(n)] for _ in range(m)]
# print(lcs(s1,s2,0,m-1,n-1,dp))


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
    str1 = ""
    i = n1-1
    j = n2-1
    ans = 0
    max1 = 0
    while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                str1 += s1[i]
                ans += 1
                max1 = max(ans,max1)
                i -=1 
                j -=1 
            elif i > 0 and dp[i-1][j] >= dp[i][j-1]:
                i -= 1
                ans = 0
                str1 = ""
            else:
                j -= 1
                ans = 0
                str1 = ""
    return [max1]

s1 = "abssdcpqru"
s2 = "sjdgvgvvpqru"
m = len(s1)
n = len(s2)
dp = [[-1 for _ in range(n)] for _ in range(m)]
result = lcs(s1,s2,dp)
print(result)