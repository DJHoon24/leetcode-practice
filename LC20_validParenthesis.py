class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Create stack with List
        for char in s:
            if (char == '(' or char == '{' or char == '['):
                stack.append(char) # Add to stack
            elif not stack: # If stack is empty when seeing a closing bracket, not valid
                return False
            elif char == ')':
                if stack.pop() != '(':
                    return False
            elif char == '}':
                if stack.pop() != '{':
                    return False
            elif char == ']':
                if stack.pop() != '[':
                    return False
        
        return not stack