# link: https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        curr = 1
        for n in nums:
            output.append(curr)
            curr *= n
        
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= curr
            curr *= nums[i]
        
        return output
