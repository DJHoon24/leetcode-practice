# Link: https://leetcode.com/problems/restore-the-array/

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(idx):
            if (idx >= len(s)):
                return 1
            if (int(s[idx]) == 0):
                return 0
            total = 0
            currNumber = 0
            for i in range(idx, len(s)):
                currNumber *= 10
                currNumber += int(s[i])
                if (currNumber > k):
                    break
                total += dp(i + 1)
            
            return total % MOD

        
        return dp(0)

            