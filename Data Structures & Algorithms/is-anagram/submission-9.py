class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scontainer = {}
        tcontainer = {}
        for char in s:
            if char in scontainer:
                scontainer[char] = 1 + scontainer[char]
            else:
                scontainer[char] = 1
            
        for char in t:
            if char in tcontainer:
                tcontainer[char] = 1 + tcontainer[char]
            else:
                tcontainer[char] = 1
        return scontainer == tcontainer
