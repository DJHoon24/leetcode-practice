# Link: https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(idx):
            if(idx >= len(nums)):
                return 0
            return max(nums[idx] + dp(idx + 2), dp(idx + 1))
        
        return dp(0)