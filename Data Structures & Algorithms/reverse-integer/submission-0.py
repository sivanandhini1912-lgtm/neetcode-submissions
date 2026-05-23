class Solution:
    def reverse(self, x: int) -> int:
        MIN=-(2**31)
        MAX=2**31-1
        sign = -1 if x<0 else 1
        x=abs(x)
        rev=0

        while x:

            r=x%10
            rev=rev*10+r
            x//=10
        
        rev= sign*rev
        
        if rev<MIN or rev>MAX:
            
            return 0

        

        return rev



       