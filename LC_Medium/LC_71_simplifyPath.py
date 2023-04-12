# Link: https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        currentString = "/"
        for char in path:
            if (char == '/'):
                # Check current string
                # If current string is .. CLEAR THE STACK
                # If current string is . continue dont add anything to stack
                # If current string is "/" continue
                # Else add it to the stack
                if (currentString == "/.."):
                    currentString = "/"
                    if stack:
                        stack.pop()
                elif (currentString == "/."):
                    currentString = "/"
                    continue
                elif (currentString == "/"):
                    continue
                else:
                    stack.append(currentString)
                    currentString = "/"
            else:
                currentString += char
        
        if (currentString == "/.." and stack):
            stack.pop()
        elif (currentString != "/" and currentString != "/." and currentString != "/.."):
            stack.append(currentString)
        finalPath = ""
        for pathName in stack:
            finalPath += pathName
        
        if (finalPath == ""):
            return "/"
        return finalPath