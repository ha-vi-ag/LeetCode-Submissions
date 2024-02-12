class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        count = Counter()
        length = []
        for word in words:
            length.append(len(word))
            for ch in word:
                count[ch] += 1
                
        length.sort()
        pairs = 0 
        for v in count.values():
            pairs += v // 2 
        
        cnt = 0
        for i in length:
            if pairs >= i // 2:
                pairs -= i // 2
                cnt += 1
        
        return cnt
        