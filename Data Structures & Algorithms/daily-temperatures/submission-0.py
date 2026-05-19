class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result=[0]*len(temperatures)
        stack=[]

        for i,temp in enumerate(temperatures):

            while stack and temp>stack[-1][1]:

                prevIndex,prevTemp=stack.pop()
                result[prevIndex]=i-prevIndex

            stack.append((i,temp))
        return result