# Link: https://leetcode.com/problems/house-robber-iii/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(root):
            if (root == None):
                return 0
            left_grandchildren = 0
            right_grandchildren = 0
            if (root.left):
                left_grandchildren = dp(root.left.right) + dp(root.left.left)
            if (root.right):
                right_grandchildren = dp(root.right.right) + dp(root.right.left)
            choose = root.val + left_grandchildren + right_grandchildren
            dont_choose = dp(root.left) + dp(root.right)
            return max(choose, dont_choose)
        return dp(root)