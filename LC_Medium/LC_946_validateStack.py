# Link: https://leetcode.com/problems/validate-stack-sequences/
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        length = len(popped)
        popIndex = 0
        pushIndex = 0
        stack = []
        while (popIndex != length):
            if stack:
                topOfStack = stack.pop()
                if (topOfStack == popped[popIndex]):
                    popIndex += 1
                    continue
                elif (pushIndex != length):
                    stack.append(topOfStack)
                    stack.append(pushed[pushIndex])
                    pushIndex += 1
                else:
                    return False
            elif(pushIndex != length):
                stack.append(pushed[pushIndex])
                pushIndex += 1
            else:
                return False
        
        return True