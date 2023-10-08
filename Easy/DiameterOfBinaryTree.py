# link: https://leetcode.com/problems/diameter-of-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        if root:
            self.height(root)
            return self.diameter
        return 0
        
    def height(self, node):
        if hasattr(node, "height"):
            return node.height
        lh, rh = 0, 0
        if node.left:
            lh = self.height(node.left) + 1
        if node.right:
            rh = self.height(node.right) + 1
        node.height = max(lh, rh)
        self.diameter = max(self.diameter, lh + rh)
        return max(lh, rh)
