def decode_message( s: str, p: str) -> bool:

  def is_match(secret, pattern):
    m = len(secret)
    n = len(pattern)

    # Create a 2D DP array with (m+1) x (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty pattern matches empty secret
    dp[0][0] = True

    # Fill the first row for patterns that consist solely of '*'
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == secret[i - 1] or pattern[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]

# Example test cases
print(is_match("aa", "a"))       # Output: False
print(is_match("aa", "*"))       # Output: True
print(is_match("cb", "?a"))      # Output: False
print(is_match("adceb", "*a*b")) # Output: True
print(is_match("acdcb", "a*c?b"))# Output: False
