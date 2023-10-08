# link: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        count = {}
        two_sum = {}

        set_nums = list(set(nums))
        for n in set_nums:
            count[n] = nums.count(n)
    
        ans = []
        l = len(set_nums)
        for i in range(l):
            a = set_nums[i]
            if count[a] >= 3 and a == 0:
                ans.append((a, a, a))
            for j in range(i+1, l):
                b = set_nums[j]
                c = 0 - a - b
                if c not in count:
                    continue
                if a == c and b == c:
                    if count[c] < 3:
                        continue
                if a == c or b == c:
                    if count[c] < 2:
                        continue
                ans.append(tuple(sorted((a, b, c))))
        
        return set(ans)
