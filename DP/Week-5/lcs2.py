def lcs2(s1,s2,dp):
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
    while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                str1 += s1[i]
                i -=1 
                j -=1 
            elif i > 0 and dp[i-1][j] >= dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    return str1[::-1]
s1 = "hsjnpq"
s2 = "spdbcsudycbsdjhcbsdq"
n1 = len(s1)
n2 = len(s2)
dp = [[0 for _ in range(n2)] for _ in range(n1)]
print(lcs2(s1,s2,dp))