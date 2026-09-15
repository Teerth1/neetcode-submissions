class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ok = defaultdict(list)
        
        for s in strs:
            a = [0] * 26
            for c in s:
                a[ord(c) - ord("a")] += 1
            
            ok[tuple(a)].append(s) 
       
        return list(ok.values())