class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)
        ans = -1
        for i in range(len(s)):
            cur = s[i]
            d[cur] += 1
            
            if d[cur] >= 3:
                ans = max(ans, len(cur))
                    
            for j in range(i + 1, len(s)):
                if cur[-1] != s[j]:
                    break
                cur += s[j]
                d[cur] += 1
            
                if d[cur] >= 3:
                    ans = max(ans, len(cur))
                    
        return ans