class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        con ={}
        for i in range(len(nums)):
            complement = target -nums[i]
            if nums[i] in con:
                return [con[nums[i]], i]
            con[complement] = i