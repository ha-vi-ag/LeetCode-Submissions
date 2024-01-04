class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {} 
        for i in nums:
            d[i] = d.get(i,0) + 1 
            
        ans = 0
        for key in d:
            if d[key] == 1:
                return -1 
            
            ans += d[key] // 3
            d[key] %= 3 
            if d[key] > 0:
                ans += 1 
                
        return ans