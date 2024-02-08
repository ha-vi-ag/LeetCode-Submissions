class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums)) 
        n = len(nums)
        cnt = 0
        ones = sorted(map(lambda x: bin(x).count('1'), nums))
        
        arr = []

        for i in ones:
            ind = bisect.bisect_left(arr, k - i) 
            
            cnt += (len(arr) - ind) * 2
            
            if i * 2 >= k: cnt += 1
            
            arr.append(i) 
            
        return cnt 