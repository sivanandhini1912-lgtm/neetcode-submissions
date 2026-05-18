class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        n = len(s)

        for i in range(n):

            seen = ""

            for j in range(i, n):

                if s[j] in seen:
                    break

                seen += s[j]

                if len(seen)>max_len:


                    max_len =  len(seen)

        return max_len