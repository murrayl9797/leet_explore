# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        self.count = 0

        def traverse(node):

            if not node:
                return None

            # Check if leaf
            if not node.left and not node.right:
                self.count += 1
                return node.val

            l_sub = traverse(node.left)
            r_sub = traverse(node.right)

            # Case 1 (all equal)
            if l_sub and r_sub and l_sub == r_sub and l_sub == node.val:
                self.count += 1
                return node.val

            # Case 2 (no l_sub)
            elif not l_sub and r_sub == node.val:
                self.count += 1
                return node.val

            elif not r_sub and l_sub == node.val:
                self.count += 1
                return node.val

            else:
                return -1001

        traverse(root)

        return self.count