class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stacktemp, stackind = stack.pop()
                ans[stackind] = i - stackind
            stack.append([temp, i])
        return ans