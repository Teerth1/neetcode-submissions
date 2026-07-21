class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        l = 0
       
        if not s:
            return 0
        if len(s) == 1:
            return 1
            
        longest = 0
        for i in range(0,len(s)):
            
            if s[i] not in a:
                a.add(s[i])
            else:
                while s[l] != s[i]:
                    a.remove(s[l])
                    l += 1
               
                l += 1
            longest = max((i - l) + 1,longest)
        return longest