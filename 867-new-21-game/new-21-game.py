class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        windowSum = 0.0
        ans = 0.0
        for i in range(1, n + 1):
            if i - 1 < k:
                windowSum += dp[i - 1]
            if i - 1 - maxPts >= 0 and (i - 1 - maxPts) < k:
                windowSum -= dp[i - 1 - maxPts]
            dp[i] = windowSum / maxPts
            if i >= k:
                ans += dp[i]
        return ans

        