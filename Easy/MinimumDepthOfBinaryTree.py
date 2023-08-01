# link: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# runtime: 770 ms
# memory: 92 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 1
        queue = []
        if not root:
            return 0
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        if not queue:
            return 1

        while queue:
            newqueue = []
            depth += 1
            while queue:
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            queue = newqueue
