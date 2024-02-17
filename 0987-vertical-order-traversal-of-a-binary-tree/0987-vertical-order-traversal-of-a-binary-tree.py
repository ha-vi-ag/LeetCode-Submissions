# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list) 
        
        bfs = [(root, 0)] 
        
        while bfs:
            l = len(bfs) 
            cur = defaultdict(list) 
            updated = []
            for i in range(l):
                node, col = bfs.pop() 
                cur[col].append(node.val) 
                if node.left: updated.append((node.left, col-1)) 
                if node.right: updated.append((node.right, col+1)) 
                    
            for col in cur:
                ans[col] += sorted(cur[col])
            bfs = updated
            
        res = [] 
        
        for col in sorted(ans):
            res.append(ans[col])
            
        return res