class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        visited = {} 
        m, n = len(maze), len(maze[0])
        r, c = entrance
        queue = [(r, c)]
        visited[r, c] = 1 
        
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]] 
        
        op = 0
        while queue:
            l = len(queue) 
            cur = [] 
            for i in range(l):
                r, c = queue.pop()  
                for j in range(4):
                    rd, cd = dir[j] 
                    if 0 <= r + rd < m and 0 <= c + cd < n:
                        if (r + rd, c + cd) not in visited and maze[r+rd][c+cd] == '.':
                            if r + rd == 0 or r + rd == m-1 or c+cd == 0 or c+cd == n-1:
                                return op + 1
                            cur.append((r + rd, c + cd))
                            visited[r+rd,c+cd] = 1 
            queue = cur
            op += 1
            
        return -1