class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        originalLength = len(nums)
        setLength = len(set(nums))
        return originalLength != setLength