# link: https://leetcode.com/problems/permutations/
# runtime: 14 ms
# memory: 13.43 MB

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr_lst = [[nums[0]]]
        n = len(nums)
        for i in range(1,n):
            num = nums[i]
            new_curr_lst = []
            for lst in curr_lst:
                for j in range(i+1):
                    new_lst = list(lst)
                    new_lst.insert(j, num)
                    new_curr_lst.append(new_lst)
            curr_lst = new_curr_lst

        return curr_lst
