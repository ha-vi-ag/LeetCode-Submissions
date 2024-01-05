class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n^2 algorithm
        n = len(nums)
        dp = [[-1] * n for i in range(n)]
        def solve(i, j):
            if i >= n: return 0 
            ans = 0
            if j != -1 and dp[i][j] != -1: return dp[i][j]
            if nums[i] > nums[j] or j == -1:
                ans = 1 + solve(i + 1, i)
            ans = max(ans, solve(i+1, j)) 
            dp[i][j] = ans
            return ans
        
        return solve(0, -1)
            
