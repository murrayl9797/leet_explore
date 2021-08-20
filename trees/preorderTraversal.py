# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Base case
        if root is None:
            return []

        # Recursive cases
        left_arr = self.preorderTraversal(root.left)
        right_arr = self.preorderTraversal(root.right)

        # Combine
        return  [root.val] + left_arr + right_arr


