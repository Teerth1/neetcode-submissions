import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # O(n) time 
        heap = []
        for n, v in counter.items():
            heapq.heappush(heap,(-v,n)) #logn
        res = []
        for i in range(k):
            val = heapq.heappop(heap)
            x,y = val
            print(val)
            res.append(y)
                
        return res


                