# link: https://leetcode.com/problems/unique-paths/
# runtime: 14 ms
# memory: 13.22 MB

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        tbl = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            tbl[0][i] = 1
        for i in range(m):
            tbl[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                tbl[i][j] = tbl[i-1][j] + tbl[i][j-1]
        return tbl[m-1][n-1]
