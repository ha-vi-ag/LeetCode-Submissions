class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(list)
        ans = -1
        cur = s[0] 
        for i in range(1, len(s)):
            if s[i] != cur[-1]:
                d[cur[-1]].append(len(cur))
                cur = ''
            cur += s[i]
            
        d[cur[-1]].append(len(cur)) 
        
        for l in d.values():
            l.sort(reverse=1)
            if len(l) >= 3:
                ans = max(ans, l[2])
            if len(l) >= 2:
                if l[0] > l[1]:
                    ans = max(ans, l[1])
                elif l[1] > 1:
                    ans = max(ans, l[1]-1)
            if len(l) >= 1 and l[0] >= 3:
                ans = max(ans, l[0]-2)
                
        return ans
            
            
            
                
            
            