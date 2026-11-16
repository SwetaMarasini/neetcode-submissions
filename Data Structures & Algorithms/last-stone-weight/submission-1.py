class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:  #-8, -7
                heapq.heappush(stones, first - second)
        stones.append(0) #cover the egde case when our stone stack is empty
        return abs(stones[0])
