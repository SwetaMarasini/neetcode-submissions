class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in container:
                container[nums[i]] +=1
            else:
                container[nums[i]] = 1
            
        sorted_num = sorted(container, key = lambda n: container[n], reverse = True)
        return sorted_num[:k]