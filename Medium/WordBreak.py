# link: https://leetcode.com/problems/word-break/
# runtime: 20 ms
# memory: 13.3 MB

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        canStart = [False] * (len(s)+1)
        canStart[0] = True  # True if new word can start from that index
        maxWordLen = max(map(len, wordDict))

        for i in range(1, len(s)+1):
            start = max(0, i-maxWordLen)
            for j in range(start, i+1):
                word = s[j:i]
                if word in wordDict and canStart[j]:
                    canStart[i] = True
        
        return canStart[-1]
