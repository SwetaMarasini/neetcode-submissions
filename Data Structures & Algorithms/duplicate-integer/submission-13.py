class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = len(set(nums))
        return num != len(nums)