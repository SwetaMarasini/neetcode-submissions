class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d2char = { "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5" : "jkl",
                    "6" :"mno",
                    "7" : "pqrs",
                    "8" : "tuv", 
                    "9" : "wxyz"}
        def backtrack(i, curStack):
            if len(curStack) == len(digits):
                res.append(curStack)
                return
            for c in d2char[digits[i]]:
                backtrack(i+1, curStack + c)

        if digits:
            backtrack(0,"")
        return res