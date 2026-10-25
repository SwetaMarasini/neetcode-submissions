class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        container = set()
        maxlength = 0
        while right < len(s):
            if s[right] not in container:
                container.add(s[right])
                right +=1 
                length = right - left
                maxlength = max(length, maxlength)
            else:
                    container.remove(s[left])
                    left +=1
        return maxlength

