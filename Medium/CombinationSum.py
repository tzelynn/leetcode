# link: https://leetcode.com/problems/combination-sum/
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.backtrack(candidates, target, 0, len(candidates))

    def backtrack(self, candidates, target, ind, len_cdd):
        if target == 0:
            return [[]]
        if target < 0 or ind >= len(candidates):
            return None
        output = []
        for i in range(ind, len_cdd):
            use_cdd = self.backtrack(candidates, target-candidates[i], i, len_cdd)
            if use_cdd is not None:
                for lst in use_cdd:
                    lst.append(candidates[i])
                    output.append(lst)
        
        return output
