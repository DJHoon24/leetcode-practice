# Link: https://leetcode.com/problems/triangle/
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(depth, index):
            if (depth == len(triangle)):
                return float('inf')
            if (index == len(triangle[depth])):
                return float('inf')
            if (depth == (len(triangle) - 1)):
                return triangle[depth][index]
            
            return triangle[depth][index] + min(dp(depth + 1, index), dp(depth + 1, index + 1))
        return dp(0, 0)

