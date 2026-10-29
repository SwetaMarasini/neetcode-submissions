class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l <=r:
            mid = (l+r)//2
            if target ==nums[mid]:
                return mid
            elif target <= nums[mid]:
                if nums[l] <= nums[mid] and target < nums[l]:
                    l = mid +1
                else:
                    r = mid -1
            else:
                if nums[mid] <= nums[r] and target > nums[r]:
                    r = mid -1
                else:
                    l = mid +1
        return -1