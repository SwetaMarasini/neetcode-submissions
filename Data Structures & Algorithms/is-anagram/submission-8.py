class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters ={}
        for letter in s:
            sLetters[letter] = sLetters.get(letter,0) +1
        tLetters ={}
        for letter in t:
            tLetters[letter] = tLetters.get(letter,0) +1
        return sLetters ==tLetters