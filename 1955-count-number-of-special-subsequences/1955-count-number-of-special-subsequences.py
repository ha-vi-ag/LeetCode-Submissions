class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0, 0, 0] 
        MOD = 10 ** 9 + 7
        for i in nums:
            if i == 0: 
                dp[i] = 1 + 2 * dp[i] % MOD 
            else: 
                dp[i] = (2 * dp[i] % MOD + dp[i-1]) % MOD
                
        return dp[-1] % MOD