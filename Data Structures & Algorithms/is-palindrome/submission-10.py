class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1 
        if len(s) == 0:
            return False
        while l < r:
            while l < r and not s[l].isalnum():
                l = l + 1
            while l < r and  not s[r].isalnum():
                r = r - 1
            if s[l].upper() != s[r].upper():
                return False
            else:
                l += 1
                r -= 1
        return True