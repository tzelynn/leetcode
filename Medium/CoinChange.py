# link: https://leetcode.com/problems/coin-change/
# runtime: 795 ms
# memory: 13.89 MB

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
    
        tbl = [0] * (amount+1)
        for c in coins:
            if c <= amount:
                tbl[c] = 1
        for a in range(1, amount+1):
            for c in coins:
                if c >= a:
                    continue
                num = tbl[a-c]
                if num == 0:
                    continue
                if tbl[a] == 0:
                    tbl[a] = num + 1
                else:
                    tbl[a] = min(tbl[a], num+1)

        if tbl[amount] == 0:
            return -1
        else:
            return tbl[amount]
