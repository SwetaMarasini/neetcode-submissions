class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', '}': '{', ']':'['}
        stack = []
        for string in s:
            if string in ('(', '{', '['):
                stack.append(string)
            else:
                if not stack:
                    return False
                lastsym = stack.pop()
                if matches[string] != lastsym:
                    return False
        return not stack
        