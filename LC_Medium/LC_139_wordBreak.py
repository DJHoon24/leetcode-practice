# Link: https://leetcode.com/problems/word-break/

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(substring):
            if substring == "":
                return True
            for word in wordDict:
                if word == substring[0:len(word)]:
                    if dp(substring[len(word)::]):
                        return True
            return False
        
        return dp(s)