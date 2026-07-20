class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r] 
        count = 0
        while l < r:
            if maxRight < maxLeft:
                r -= 1
             
                if maxRight - height[r] >= 0:
                    count += maxRight - height[r]
               
            
                maxRight = max(maxRight, height[r])
            else:
                l += 1
                if maxLeft - height[l] >= 0:
                    count += maxLeft - height[l]
                maxLeft = max(maxLeft, height[l])
        return count