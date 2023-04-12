# Link: https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if (node is None):
            return None
        visited = [False for i in range(101)]
        cloneGraph = [None for i in range(101)]
        root = Node(node.val, [])
        cloneGraph[root.val] = root
        visited[root.val] = True
        queue = [node]

        while (queue):
            currNodeOriginalGraph = queue.pop(0)
            currNodeNewGraph = cloneGraph[currNodeOriginalGraph.val]
            for neighbour in currNodeOriginalGraph.neighbors:
                if (not visited[neighbour.val]):
                    cloneGraph[neighbour.val] = Node(neighbour.val, [])
                    visited[neighbour.val] = True
                    queue.append(neighbour)
                currNodeNewGraph.neighbors.append(cloneGraph[neighbour.val])
        
        return root
        