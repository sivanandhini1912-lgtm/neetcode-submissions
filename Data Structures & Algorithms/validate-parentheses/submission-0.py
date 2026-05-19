class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        closeToOpen={
        ")" : "(",
        "]" : "[",
        "}" : "{"
        }

        for ch in s:

            if ch in "([{":
                stack.append(ch)
            
            else:
                
                if not stack:
                    return False
                
                if stack[-1]!=closeToOpen[ch]:
                    return False
                stack.pop()
        
        return len(stack)==0