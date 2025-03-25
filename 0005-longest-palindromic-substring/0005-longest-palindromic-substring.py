class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the longest palindrome found
            return s[left + 1:right]
        
        longest = ""
        
        for i in range(len(s)):
            # Check for odd length palindromes (single character center)
            palindrome1 = expand_around_center(i, i)
            # Check for even length palindromes (two characters center)
            palindrome2 = expand_around_center(i, i + 1)
            
            # Choose the longer of the two
            longest = max(longest, palindrome1, palindrome2, key=len)
        
        return longest
