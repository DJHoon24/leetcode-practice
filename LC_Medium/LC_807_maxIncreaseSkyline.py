# Link: https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxValuesRows = []
        maxValuesCols = [0 for _ in range(len(grid))]
        
        for i, row in enumerate(grid):
            maxRowNumber = 0
            for j, col in enumerate(row):
                maxValuesCols[j] = max(maxValuesCols[j], col)
                maxRowNumber = max(maxRowNumber, col)
            maxValuesRows.append(maxRowNumber)
        
        totalIncrease = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                totalIncrease += (min(maxValuesRows[i], maxValuesCols[j]) - col)
        return totalIncrease