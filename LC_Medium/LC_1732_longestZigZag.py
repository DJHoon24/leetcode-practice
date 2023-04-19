# Link: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
      def dfs(root, left, length):
        if root is None: # Once I'm at a null case I want to return the number of edges
          return length - 1
        if left: # In left case I either go right and increase my count or violate and reset count to 1
          return max(dfs(root.right, False, length + 1), dfs(root.left, True, 1))
        # In right case I either go left and increase my count or violate and reset my count to 1
        return max(dfs(root.right, False, 1), dfs(root.left, True, length + 1))
      
      return max(dfs(root, True, 0), dfs(root, False, 0))
        