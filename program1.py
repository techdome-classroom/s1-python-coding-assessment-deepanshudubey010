def numIslands(grid):
    if not grid:
        return 0

    num_islands = 0

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return

        grid[i][j] = 'W'  # Mark the land as water

        # Explore all four directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':
                num_islands += 1
                dfs(i, j)

    return num_islands

dispatch1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
print(numIslands(dispatch1))  # Output: 1

dispatch2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]
print(numIslands(dispatch2))  # Output: 3

