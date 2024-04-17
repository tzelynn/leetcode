# link: https://leetcode.com/problems/number-of-islands/
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    self.traverse(grid, i, j)
        
        return count
    
    def traverse(self, grid, i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
            return
        if grid[i][j] == "1":
            grid[i][j] = "X"
            self.traverse(grid, i+1, j)
            self.traverse(grid, i-1, j)
            self.traverse(grid, i, j+1)
            self.traverse(grid, i, j-1)
