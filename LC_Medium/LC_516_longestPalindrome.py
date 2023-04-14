# Link: https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(leftIdx, rightIdx):
            if (leftIdx > rightIdx):
                return 0
            if(leftIdx == rightIdx):
                return 1
            if (s[leftIdx] == s[rightIdx]):
                return 2 + dp(leftIdx + 1, rightIdx - 1)
            else:
                return max(dp(leftIdx+1, rightIdx), dp(leftIdx, rightIdx-1))
        return dp(0, (len(s)-1))