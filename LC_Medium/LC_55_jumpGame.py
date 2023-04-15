# Link: https://leetcode.com/problems/jump-game

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachableIndex = 0
        for i in range(len(nums)):
            if(maxReachableIndex < i):
                return False
            maxReachableIndex = max(maxReachableIndex, nums[i] + i)
        
        return True
    

"""
DP Top Down Solution TLEs because of O(n^2) computation
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        from functools import cache
        @cache
        def dp(index):
            if (index >= (length - 1)):
                return True
            if (nums[index] == 0):
                return False
            for i in range(1, nums[index] + 1):
                if(dp(index + i)):
                    return True
            
            return False
        
        return dp(0)
"""