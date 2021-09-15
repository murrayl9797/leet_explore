# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Define helper
        def findStrPath(seen, target, curr):
            # print(seen, target, curr)

            # Base
            if not curr:
                return None

            if curr.val == target:
                return seen

            # Recursive
            l = findStrPath(seen + [curr.left], target, curr.left) if curr.left else None
            r = findStrPath(seen + [curr.right], target, curr.right) if curr.right else None

            return l or r

        # Get paths
        p_path = findStrPath([root], p.val, root)
        q_path = findStrPath([root], q.val, root)

        b = len(p_path) > len(q_path)

        longer = p_path if b else q_path
        shorter = q_path if b else p_path

        # Find answer
        for node in longer[::-1]:

            if node in shorter:
                return node
