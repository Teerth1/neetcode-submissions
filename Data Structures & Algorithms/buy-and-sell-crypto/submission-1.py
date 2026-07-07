class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        
        left = 0  # buy pointer
        maxProfit = 0
        
        for right in range(len(prices)):
            # If we found a cheaper day to buy, update left
            if prices[right] < prices[left]:
                left = right
            
            # Calculate profit if we sell today
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        
        return maxProfit