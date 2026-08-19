class Solution:
    def isValid(self, s: str) -> bool:
        match= { ')':'(', '}':'{', ']':'['}
        con =[]
        for char in s:
            if char in "({[":
                con.append(char)
            else:
                if not con:
                    return False
                top = con.pop()
                if top != match[char]:
                    return False
        return not con