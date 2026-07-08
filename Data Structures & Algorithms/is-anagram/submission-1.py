from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        a = Counter(s)
        b = Counter(t)

        if len(s) != len(t):
            return False
        

        for i in range(len(s)):
            if a.get(s[i],0) != b.get(s[i],0):
                return False
        return True

        
