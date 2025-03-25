class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # Create a DP table where dp[i][j] represents whether s[0..i] matches p[0..j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string s matches empty pattern p
        dp[0][0] = True
        
        # Handle cases where pattern p starts with 'a*', 'b*' etc., for empty s
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Case 1: '*' represents zero occurrence of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # Case 2: '*' represents one or more occurrences of the preceding element
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[m][n]
