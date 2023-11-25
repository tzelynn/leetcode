# link: https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        traverse = [root]
        root.lb = None
        root.ub = None
        root.was = None
        while traverse:
            curr = traverse.pop()
            if curr.left:
                left = curr.left
                if left.val >= curr.val:
                    return False
                if curr.lb and left.val <= curr.lb:
                    return False
                traverse.append(left)
                left.lb = curr.lb
                left.ub = curr.val
            if curr.right:
                right = curr.right
                if right.val <= curr.val:
                    return False
                if curr.ub and right.val >= curr.ub:
                    return False
                traverse.append(curr.right)
                right.lb = curr.val
                right.ub = curr.ub

        return True
