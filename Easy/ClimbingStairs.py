# link: https://leetcode.com/problems/climbing-stairs/description/
# runtime: 11 ms
# memory: 13.45 MB

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        tbl = [0] * (n+1)
        tbl[1] = 1
        tbl[2] = 2
        for s in range(3, n+1):
            tbl[s] = tbl[s-1] + tbl[s-2]

        return tbl[n]
