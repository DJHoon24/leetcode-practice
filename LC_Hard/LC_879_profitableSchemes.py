# Link: https://leetcode.com/problems/profitable-schemes/

from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        length = len(group)
        MOD = 10**9 + 7
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(index, n, currProfit):
            if (n < 0):
                return 0
            if (currProfit >= minProfit) and (index >= length):
                return 1
            if (index >= length):
                return 0
            return dp(index + 1, n - group[index], min(currProfit + profit[index], minProfit)) + dp(index + 1, n, currProfit)
        
        return dp(0, n, 0) % MOD