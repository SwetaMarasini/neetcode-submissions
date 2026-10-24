class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                first_num = stack.pop()
                second_num = stack.pop()
                if token =='+':
                    stack.append(first_num + second_num)
                elif token =='-':
                    stack.append(second_num - first_num)
                elif token =='*':
                    stack.append(first_num * second_num)
                else:
                    stack.append(int(second_num / first_num))
        return stack.pop()