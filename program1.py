class Solution:

    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        island_count = 0

        # DFS function to explore the island
        def dfs(r, c):
            # Check for out of bounds and water
            if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.grid[r][c] == 'W':
                return
            
            # Mark the land as visited
            self.grid[r][c] = 'W'  # Change 'L' to 'W'
            
            # Explore all four directions
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        # Traverse the grid
        for r in range(self.rows):
            for c in range(self.cols):
                # If we find land, it's a new island
                if self.grid[r][c] == 'L':
                    island_count += 1
                    dfs(r, c)  # Use DFS to mark all connected land

        return island_count
