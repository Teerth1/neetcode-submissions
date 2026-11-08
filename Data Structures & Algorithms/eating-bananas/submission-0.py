class Solution:
    
    def calculatefunc(self,mid,piles):
        sum = 0
        for i in range(len(piles)):
            sum += math.ceil(piles[i] / mid) 
        return sum
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l = 1
        r = k
        mi = k 
        while l <= r:
            mid = (l+r)//2
            calc = self.calculatefunc(mid,piles)
            if calc <= h:
                r = mid - 1
                mi = mid
            elif calc > h:
                l = mid + 1
                
        return mi
            

                