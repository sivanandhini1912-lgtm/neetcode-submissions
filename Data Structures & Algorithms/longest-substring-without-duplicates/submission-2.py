class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        max_len=0
        left=0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            current_win_len=right-left+1
            max_len=max(max_len,current_win_len)
        return max_len

       