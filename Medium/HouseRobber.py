# link: https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        table = [0, 0]

        for num in nums:
            rob = table[1] + num
            skip = max(table)
            table = [rob, skip]
        
        return max(table)
