class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        longest = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in a:
                length = 0
                j = 0
                while (nums[i] + j) in a:
                    length += 1
                    j +=1
                longest = max(length,longest)
    

        return longest
            