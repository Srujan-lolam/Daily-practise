def stock_2(prices):
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    def getMaxProfit(idx,buy):
        if idx == n:
            return 0
        if dp[idx][buy] != -1:
            return dp[idx][buy]
        dp[idx][buy] = 0
        if buy == 0:
            dp[idx][buy] = max(getMaxProfit(idx+1,0),-prices[idx] + getMaxProfit(idx+1,1))  
        if buy == 1 :
            dp[idx][buy] = max(getMaxProfit(idx+1,1),prices[idx] + getMaxProfit(idx+1,0))
        return dp[idx][buy]
    return getMaxProfit(0,0)
prices = [1,2,4]
print(stock_2(prices))

# //There are many variants on this problem . solved all of them in leetcode as most of them are unsolved before 

    