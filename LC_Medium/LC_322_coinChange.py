# Link: https://leetcode.com/problems/coin-change/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(amount):
            if (amount == 0):
                return 0
            if (amount < 0):
                return float('inf')
            minCoins = float('inf')
            for coin in coins:
                minCoins = min(minCoins, 1 + dp(amount-coin))
            
            return minCoins
        
        totalCoins = dp(amount)
        if totalCoins == float('inf'):
            return -1
        return totalCoins