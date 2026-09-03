class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        if not nums:
            return 0
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in seen:
            
                count = 1
                curr_num = nums[i]

                while curr_num in seen:
                    
                    count = count + 1
                    curr_num += 1
                maxCount = max(maxCount,count) 
                        
                    
                
                
        return maxCount - 1