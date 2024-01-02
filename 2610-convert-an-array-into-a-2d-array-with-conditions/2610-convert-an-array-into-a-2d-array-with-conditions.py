class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        maxi = 0 
        d = defaultdict(int)
        for i in nums:
            d[i] += 1 
            maxi = max(maxi, d[i]) 
        
        ans = []
        while maxi > 0:
            maxi -= 1
            ans.append([])
            
            for i in d:
                if d[i] > 0:
                    d[i] -= 1
                    ans[-1].append(i)
                    
        return ans
            
            
        