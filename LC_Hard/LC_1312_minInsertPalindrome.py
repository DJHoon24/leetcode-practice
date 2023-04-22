# Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution:
    def minInsertions(self, s: str) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(i, j):
            if (j <= i):
                return 0
            if (s[i] == s[j]):
                return dp(i + 1, j -1)
            return min(1 + dp(i + 1, j), 1 + dp(i, j - 1))
        
        return dp(0, len(s) - 1)