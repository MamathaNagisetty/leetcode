class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the difference (target - num) and its index
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                # Return the indices if the complement is found
                return [num_map[complement], i]
            # Otherwise, store the current number and its index
            num_map[num] = i
