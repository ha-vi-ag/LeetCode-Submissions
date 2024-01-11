class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        count = 0 
        
        for i in range(len(nums)):
            
            for j in range(i + 2, len(nums)):
                if nums[j] - nums[j-1] == nums[i + 1] - nums[i]:
                    count += 1
                else:
                    break
                    
        
        return count