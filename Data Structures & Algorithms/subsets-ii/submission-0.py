class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return res
            
            #include nums[i]
            subset.append(nums[i])
            backtracking(i+1, subset)

            #don't include nums[i]
            subset.pop()
            #backtracking(i+1, subset)

            #skip duplicate
            while  i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtracking(i+1 , subset) ##this will give us []
        backtracking(0,[])
        return res