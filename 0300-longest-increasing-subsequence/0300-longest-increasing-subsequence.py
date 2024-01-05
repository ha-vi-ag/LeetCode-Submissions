class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nlogn algorithm
        
        ans = 1
        n = len(nums)
        cur = [nums[0]]
        l = 1
        for i in range(1, n):
            ind = bisect.bisect_left(cur, nums[i]) 
            if ind != l:
                cur[ind] = nums[i] 
            else:
                cur.append(nums[i]) 
                l += 1
            ans = max(ans, ind + 1)
        return ans
            
