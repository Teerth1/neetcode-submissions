class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxHeight = 0
        height = 0
        while l < r:
            maxHeight = max((r-l) * min(heights[l],heights[r]), maxHeight)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                r = r - 1
        return maxHeight
