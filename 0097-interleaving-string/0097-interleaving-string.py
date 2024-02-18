class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2) 
        if m + n != len(s3): return False
        
        dp = {} 
        
        def solve(i, j):
            if i >= m and j >= n: 
                return True
            ind = i + j 
            
            if (i, j) in dp: return dp[i, j] 
            
            if i < m and s1[i] == s3[ind] and solve(i + 1, j):
                return True
            
            if j < n and s2[j] == s3[ind] and solve(i, j + 1):
                return True
            
            dp[i, j] = False
            return False
        
        return solve(0, 0)
    
    