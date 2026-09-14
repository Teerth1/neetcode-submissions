class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ok = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in ok:
                return [ok[complement],i]
            ok[nums[i]] = i
        