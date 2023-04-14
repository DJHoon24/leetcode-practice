# Link: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandMiddle(left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left + 1: right]
        
        substring = ""
        for i in range(len(s)):
            substring = max(substring, expandMiddle(i, i), expandMiddle(i, i + 1), key=len)
        
        return substring