# link: https://leetcode.com/problems/combinations/
# runtime: 64 ms
# memory: 18.5 MB

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        final_lst = []
        inter_lst = []
        for i in range(1, n+1):
            ori_num = len(inter_lst)
            for j in range(ori_num):
                lst = inter_lst[j]
                new_lst = list(lst)
                new_lst.append(i)
                if len(new_lst) == k:
                    final_lst.append(new_lst)
                elif k - len(new_lst) <= n - i:
                    inter_lst.append(new_lst)
            if k == 1:
                final_lst.append([i])
            else:
                inter_lst.append([i])
        
        return final_lst
