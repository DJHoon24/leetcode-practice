# Link: https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1
        
    
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight == -1 or rightHeight == -1 or (abs(leftHeight - rightHeight) > 1):
            return -1
        return max(leftHeight + 1, rightHeight + 1)