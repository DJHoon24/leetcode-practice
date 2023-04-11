# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # I Assume index 0 will never be changed, so I only change index 1 and above
        placeIndex = 1
        currentNumber = nums[0]
        for num in nums:
            if currentNumber != num:
                nums[placeIndex] = num
                currentNumber = num
                placeIndex += 1
        
        return placeIndex