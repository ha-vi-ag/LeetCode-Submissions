class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n, m = len(nums), len(l) 
        ans = []
        for i in range(m):
            a, b = l[i], r[i] 
            if b - a < 1:
                ans.append(False) 
            else:
                arr = sorted(nums[a: b + 1]) 
                for j in range(2, (b - a + 1)):
                    if arr[j] - arr[j-1] != arr[1] - arr[0]:
                        ans.append(False)
                        break
                else:
                    ans.append(True)
                    
        return ans
            