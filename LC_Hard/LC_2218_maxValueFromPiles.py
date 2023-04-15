# Link: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(pileNumber, k):
            if (k < 0):
                return float('-inf')
            if (pileNumber == len(piles)):
                return 0
            curMaxCoins = dp((pileNumber + 1), k)
            totalCoinsInPile = 0
            for i, coin in enumerate(piles[pileNumber]):
                totalCoinsInPile += coin
                totalPileValueChoosingCoin = totalCoinsInPile + dp((pileNumber + 1), (k - (i + 1)))
                curMaxCoins = max(curMaxCoins, totalPileValueChoosingCoin)
            return curMaxCoins
        return dp(0, k)