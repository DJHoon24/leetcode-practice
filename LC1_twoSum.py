class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possibleTargets = {}
        for i, num in enumerate(nums):
            if num in possibleTargets:
                return [possibleTargets[num], i]
            possibleTargets[target-num] = i
        return [-1, -1]