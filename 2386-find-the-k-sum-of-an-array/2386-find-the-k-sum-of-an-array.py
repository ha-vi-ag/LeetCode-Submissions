class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        
        total = 0
        n = len(nums)
        for i in range(n):
            total += max(0, nums[i]) 
            nums[i] = abs(nums[i])
            
        nums.sort()
        heap = [(nums[0], 0)] 
        k -= 1
        
        last = 0
        while k >= 1:
            sum, ind = heapq.heappop(heap) 
            last = sum
            
            k-=1
            if ind + 1 < n: 
                heapq.heappush(heap, (last + nums[ind + 1], ind + 1))
                heapq.heappush(heap, (last - nums[ind] + nums[ind + 1], ind + 1))
                
            
        return total - last