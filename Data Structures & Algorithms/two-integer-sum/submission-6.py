class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container = {} #remaining : index
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in container:
                return [container[nums[i]], i]
            container[complement] = i