def decode_message( s: str, p: str) -> bool:

# write your code here
  def count_islands(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def dfs(r, c):
        # Check for out of bounds and if it's water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
            return
        # Mark the land as visited by setting it to water
        grid[r][c] = 'W'
        # Explore all four possible directions (up, down, left, right)
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    # Traverse the entire grid
    for r in range(rows):
        for c in range(cols):
            # If we find land, we found an island
            if grid[r][c] == 'L':
                island_count += 1
                # Use DFS to mark all connected land as visited
                dfs(r, c)

    return island_count

# Example test cases
dispatch1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

dispatch2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]

print(count_islands(dispatch1))  
print(count_islands(dispatch2))
  
        return False
