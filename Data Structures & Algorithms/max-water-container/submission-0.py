class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxWidth = 0 
        while l < r:
            
            maxWidth = max(maxWidth,(r-l) * min(heights[l],heights[r]))
            
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l = l + 1
        
        return maxWidth