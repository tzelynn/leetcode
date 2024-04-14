# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        locs = {}
        currStart = 0
        longest = 0
        len_str = len(s)
        
        for i in range(len_str):
            letter = s[i]
            if letter in locs and locs[letter] >= currStart:
                longest = max(longest, i-currStart)
                currStart = locs[letter] + 1
            locs[letter] = i
        return max(longest, len_str-currStart)
