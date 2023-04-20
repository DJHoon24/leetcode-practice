# Link: https://leetcode.com/problems/maximum-width-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [[root, 0, 1]]
        currentLevel = -1
        leftMostIndex = 0
        rightMostIndex = 0
        maxWidth = 0
        while queue:
            currentPair = queue.pop(0)
            currentNode = currentPair[0]
            nodeLevel = currentPair[1]
            currentNodeIndex = currentPair[2]
            if currentNode is None:
                continue
            if nodeLevel != currentLevel:
                #print(nodeLevel)
                maxWidth = max(maxWidth, (rightMostIndex - leftMostIndex) + 1)
                currentLevel = nodeLevel
                leftMostIndex = currentNodeIndex
                rightMostIndex = currentNodeIndex
            if (currentNodeIndex < leftMostIndex):
                leftMostIndex = currentNodeIndex
            if (currentNodeIndex > rightMostIndex):
                rightMostIndex = currentNodeIndex
            queue.append([currentNode.left, nodeLevel + 1, currentNodeIndex * 2])
            queue.append([currentNode.right, nodeLevel + 1, (currentNodeIndex * 2) + 1])


        maxWidth = max(maxWidth, (rightMostIndex - leftMostIndex) + 1)

        return maxWidth
            
