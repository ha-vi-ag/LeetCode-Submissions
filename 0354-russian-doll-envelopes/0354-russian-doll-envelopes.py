class Node:
    def __init__(self, h, val):
        self.h = h 
        self.val = val 
        self.left = None
        self.right = None
        self.maxi = val
        self.ht = 0
        
class DSegmentTree:
    def __init__(self):
        self.root = None
        
    def addNode(self, h, val, root):
        if not root: 
            return Node(h, val) 
        
        if h <= root.h:
            root.left = self.addNode(h, val, root.left)
        else:
            root.right = self.addNode(h, val, root.right)
            
        lh = root.left.ht if root.left else 0
        rh = root.right.ht if root.right else 0
        root.ht = 1 + max(lh, rh)
        
        if lh >= rh + 2:
            temp = root.left
            root.left = temp.right
            temp.right = root
            root.ht = 1 + max((root.left.ht if root.left else 0), (root.right.ht if root.right else 0)) 
            temp.ht = 1 + max((temp.left.ht if temp.left else 0), root.ht)
            
            lm = root.left.maxi if root.left else 0
            rm = root.right.maxi if root.right else 0
            root.maxi = max(lm, rm, root.val)
            
            lm = temp.left.maxi if temp.left else 0
            rm = temp.right.maxi if temp.right else 0
            temp.maxi = max(lm, rm, temp.val)
            return temp 
        
        if rh >= lh + 2:
            temp = root.right
            root.right = temp.left
            temp.left = root
            root.ht = 1 + max((root.left.ht if root.left else 0), (root.right.ht if root.right else 0))
            temp.ht = 1 + max((temp.right.ht if temp.right else 0), root.ht)
            
            lm = root.left.maxi if root.left else 0
            rm = root.right.maxi if root.right else 0
            root.maxi = max(lm, rm, root.val)
            
            lm = temp.left.maxi if temp.left else 0
            rm = temp.right.maxi if temp.right else 0
            temp.maxi = max(lm, rm, temp.val)
            return temp 
        
        lm = root.left.maxi if root.left else 0
        rm = root.right.maxi if root.right else 0
        root.maxi = max(lm, rm, root.val)
        return root
        
    def add(self, h, val):
        self.root = self.addNode(h, val, self.root)
        
    def find(self, h):
        root = self.root 
        ans = 0
        while root:
            if root.h >= h:
                root = root.left
            else:
                ans = max(ans, root.val)
                if root.left:
                    ans = max(ans, root.left.maxi)
                root = root.right
        return ans
        
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = defaultdict(list)
        for w, h in envelopes:
            dp[w].append(h)
            
        widths = sorted(dp)
        ans = 0
        store = []
        tree = DSegmentTree()
        
        for w in widths:
            cur = []
            for h in dp[w]:
                maxi = tree.find(h) 
                cur.append((h, 1 + maxi)) 
                ans = max(ans, 1 + maxi)
                
            for h, val in cur:
                tree.add(h, val) 
                
        return ans