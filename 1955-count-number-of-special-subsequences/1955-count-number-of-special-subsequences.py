class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        zeros, twos = [0] * n, [0] * n
    
        pre = 0
        for i in range(n):
            zeros[i] = pre 
            if nums[i] == 0:
                pre += 1
        pre = 0
        for i in range(n-1, -1, -1):
            twos[i] = pre 
            if nums[i] == 2:
                pre += 1 
                
        arr = [] 
        for i in range(n):
            if zeros[i] > 0 and twos[i] > 0 and nums[i] == 1:
                arr.append((zeros[i], twos[i])) 
        ans = 0 
        MOD = 10 ** 9 + 7 
        pre = cur = 0
        
        for i in range(len(arr)):
            if i >= 2:
                pre += (pre + (pow(2, arr[i-2][0], MOD) - 1 + MOD) % MOD) % MOD
                pre %= MOD
                
            # cur += (2 ** arr[i][0] - 1) % MOD
            cur += (pow(2, arr[i][0], MOD) - 1 + MOD) % MOD
            cur %= MOD
            cur += pre 
            cur %= MOD
            
            # ans = (ans + cur * (2 ** arr[i][1] - 1) % MOD) % MOD
            ans = (ans + cur * (pow(2, arr[i][1], MOD) - 1 + MOD) % MOD) % MOD
        
        return ans % MOD