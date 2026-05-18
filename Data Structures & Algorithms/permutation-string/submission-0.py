class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            
            return False
        
        count1={}
        window={}

        for ch in s1:
           
            count1[ch]=1+count1.get(ch,0)
        
        left=0

        for right in range(len(s2)):

            window[s2[right]]=1+window.get(s2[right],0)

            if right-left+1>len(s1):

                window[s2[left]]-=1

                if window[s2[left]]==0:

               
                    del window[s2[left]]
            
                left+=1
            
           
           
            if window==count1:
               
                return True
        
        return False

