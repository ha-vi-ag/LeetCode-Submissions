class TrieNode:
    def __init__(self):
        self.isString = False
        self.children = {}
        self.count = 0

class Trie: 
    def __init__(self):
        self.root = TrieNode()
        
    def search(self, word, root):
        for i in word:
            root = root.children.get(i)
            if not root: 
                break
        return root
    
    def addWord(self, word):
        root = self.root 
        for i in word:
            if root.children.get(i) == None:
                root.children[i] = TrieNode()
            root = root.children[i]
            
        root.isString = True
        root.count += 1
        
    
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0 
        n = len(words)
        b, q = 256, 23
        
        trie = Trie()
        
        for i in range(n):
            w = words[i] 
            root = trie.root 
            l = len(w) 
            front = back = st = ""
            left = right = 0
            lefthelper = 1
            for j in range(l):
                lefthelper = lefthelper * b % q
                left, right = (left + (ord(w[j]) - 96) * lefthelper % q) % q, (right * b % q + (ord(w[l-1-j]) - 96) * b % q) % q
                front += w[j]
                st += w[j]
                back = w[l-j-1] + back
                if left == right and front == back:
                    root = trie.search(st, root)
                    st = ""
                    if not root: break
                    cnt += root.count
                       
            trie.addWord(w)
            
        return cnt