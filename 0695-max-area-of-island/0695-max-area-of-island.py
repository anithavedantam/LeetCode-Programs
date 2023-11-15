class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # loop through entire matrix, searching for 1s
        # if 1 found bfs for 1, change 1 to 0/
        # keep count of 1s seen (area), when bfs ends(visited len is 0)
        # check area and max_area, update max_area if > area
        def isValid(i, j):
            if i >= 0 and i < len(grid) and j >=0 and j < len(grid[0]):
                return True
            return False
        def bfs(i, j):
            '''return the count of 1s
            increment count each time adding to queue
            '''
            area = 0
            visited = {}
            queue = [(i, j)]
            while len(queue) != 0:
                node = queue[0]
                visited[node] = True
                x = node[0]
                y = node[1]
                grid[x][y] = 0
                queue.pop(0)
                area += 1
                if isValid(x-1, y) and (x-1, y) not in visited:
                    if grid[x-1][y] == 1:
                        queue.append((x-1, y))
                        visited[(x-1, y)] = True
                if isValid(x, y-1) and (x, y-1) not in visited:
                    if grid[x][y-1] == 1:
                        queue.append((x, y-1))
                        visited[(x, y-1)] = True
                if isValid(x+1, y) and (x+1, y) not in visited:
                    if grid[x+1][y] == 1:
                        queue.append((x+1, y))
                        visited[(x+1, y)] = True
                if isValid(x, y+1) and (x, y+1) not in visited:
                    if grid[x][y+1] == 1:
                        queue.append((x, y+1))
                        visited[(x, y+1)] = True
            return area
                
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    max_area = max(max_area, area)
        return max_area
        