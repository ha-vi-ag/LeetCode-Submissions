class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = [] 
        
        for row in bank:
            arr.append(row.count('1'))
            
        ans = 0
        pre = -1 
        for i in range(len(arr)):
            if arr[i] > 0:
                if pre != -1:
                    ans += arr[pre] * arr[i]
                pre = i 
            
        
        return ans