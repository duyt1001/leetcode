class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        dp = [0] * (len(num)+1)
        if len(num) > 0:
            dp[1] = num[0]
        for i in range(2, len(num)+1):
            dp[i] = max(dp[i-1], dp[i-2]+num[i-1])
        return dp[len(num)]

s = Solution()
mainST = [12, 13, 12, 13, 12]
print s.rob(mainST)
