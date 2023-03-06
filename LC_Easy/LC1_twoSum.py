from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possibleTargets = {}
        for i, num in enumerate(nums):
            if num in possibleTargets:
                return [possibleTargets[num], i]
            possibleTargets[target-num] = i
        return [-1, -1]

solution = Solution()
print(solution.twoSum([1,2,3,4,5], 5))

