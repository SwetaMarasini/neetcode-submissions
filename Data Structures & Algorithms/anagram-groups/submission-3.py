class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container = defaultdict(list)
        for string in strs:
            letter = [0]*26
            for char in string:
                letter[ord(char)- ord('a')] +=1
            container[tuple(letter)].append(string)

        return list(container.values())