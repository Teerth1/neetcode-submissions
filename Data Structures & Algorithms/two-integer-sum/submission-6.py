class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i in range(len(nums)):
            complement = target - nums[i]   #10 - 2  | 10 - 5 | 10 - 5
            print(complement)
            if complement in num_to_index:
                return [num_to_index.get(complement,0),i]
            num_to_index[nums[i]] = i  #2 : 0  | 5 : 1 | 
