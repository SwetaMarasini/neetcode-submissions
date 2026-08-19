class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        con = defaultdict(list)
        for num in nums:
            con[num] = con.get(num, 0) +1
        sorted_freq = sorted(con, key = lambda x: con[x], reverse = True)
        return sorted_freq[:k]