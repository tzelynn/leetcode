# link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count1 = 0
        count2 = 0

        for i in range(len(s)):
            if i % 2:
                count1, count2 = self.add(count1, count2, s[i])
            else:
                count2, count1 = self.add(count2, count1, s[i])

        return min(count1, count2)

    def add(self, counta, countb, num):
        if num == "0":
            counta += 1
        else:
            countb += 1

        return counta, countb
