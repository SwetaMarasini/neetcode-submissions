class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtracking(opened, closed):
            if n == opened and n == closed:
                res.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                backtracking(opened +1, closed)
                stack.pop()
            if n > closed and opened > closed:
                stack.append(")")
                backtracking(opened, closed +1)
                stack.pop()
        backtracking(0,0)
        return res