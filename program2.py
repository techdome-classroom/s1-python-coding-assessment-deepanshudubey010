def isMatch(message, pattern):
    # Create a 2D DP table
    dp = [[False] * (len(pattern) + 1) for _ in range(len(message) + 1)]
    
    # Empty pattern matches empty message
    dp[0][0] = True

    # Handle patterns with '*' at the beginning
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, len(message) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == message[i - 1] or pattern[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[len(message)][len(pattern)]

# Test cases
print(isMatch("aa", "a"))      # Output: False
print(isMatch("aa", "*"))      # Output: True
print(isMatch("cb", "?a"))     # Output: False
print(isMatch("adceb", "*a*b")) # Output: True
print(isMatch("acdcb", "a*c?b")) # Output: False
