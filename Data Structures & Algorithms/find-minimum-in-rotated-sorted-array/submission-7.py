class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        l , r = 0, len(nums)-1
        while l <=r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            mid = (l+r)//2
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid +1 # we held the lowest we could have we check if we have more lowest in other side
            else:
                ans = min(ans, nums[mid]) # there could be (9, -5 ,-2,0,3) lowst is in first half
                r = mid -1
        return ans