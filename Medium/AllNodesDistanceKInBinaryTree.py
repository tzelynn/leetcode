# link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# runtime: 13 ms
# memory: 13.7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        
        if k == 0:
            return [target.val]

        traverse = []
        if root.left:
            root.left.prev = root
            traverse.append(root.left)
        if root.right:
            root.right.prev = root
            traverse.append(root.right)
        root.prev = None
        
        if root.val == target.val:
            target_node = root
        else:
            target_node = None
        
        while traverse and not target_node:
            new_traverse = []
            while traverse:
                node = traverse.pop(0)
                if node.val == target.val:
                    target_node = node
                    break
                if node.left:
                    node.left.prev = node
                    new_traverse.append(node.left)
                if node.right:
                    node.right.prev = node
                    new_traverse.append(node.right)
            traverse = new_traverse
        
        if not target_node:
            return []
    
        bef = [target_node.prev]
        aft = [target_node.right, target_node.left]
        target_node.searched = True
        for i in range(k-1):
            new_bef = []
            new_aft = []
            for n in bef:
                if n:
                    new_bef.append(n.prev)
                    if n.left and not hasattr(n.left, "searched"):
                        new_aft.append(n.left)
                    if n.right and not hasattr(n.right, "searched"):
                        new_aft.append(n.right)
                    n.searched = True
            bef = new_bef
            for n in aft:
                if n:
                    new_aft.append(n.left)
                    new_aft.append(n.right)
                    n.searched = True
            aft = new_aft
        
        final_lst = []
        for n in bef:
            if n:
                final_lst.append(n.val)
        for n in aft:
            if n:
                final_lst.append(n.val)
        
        return final_lst
