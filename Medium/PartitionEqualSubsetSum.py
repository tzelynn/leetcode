# link: https://leetcode.com/problems/partition-equal-subset-sum/
# runtime: 777 ms
# memory: 13.87 MB

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        s = sum(nums)
        if s % 2:
            return False
        target = s // 2

        tbl = [False] * (target+1)
        for n in nums:
            if n == target:
                return True
            if n > target:
                return False
            old = list(tbl)
            for t in range(1, target+1):
                if old[t] and t+n <= target:
                    tbl[t+n] = True
            tbl[n] = True
        
        return tbl[target]
