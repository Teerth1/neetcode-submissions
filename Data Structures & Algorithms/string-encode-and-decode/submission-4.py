class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for i in range(len(strs)):
            a += (strs[i])
            a += "😅"

        print(a)
        return a

    def decode(self, s: str) -> List[str]:
        
        res = []
        a = ""
        for i in range(len(s)):
            print(i)
            print(s[i])
            if s[i] != "😅":
                a += s[i]
            elif s[i] == "😅":
                res.append(a)
                a = ""
        
        
        return res