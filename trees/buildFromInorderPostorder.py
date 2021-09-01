# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Base cases
        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(val=inorder.pop())


        # Recursive cases
        root_val = postorder.pop()

        # Split inorder and postorder
        root_index = inorder.index(root_val)

        l_in, r_in = inorder[:root_index], inorder[root_index+1:]
        l_post, r_post = postorder[:root_index], postorder[root_index:]


        return TreeNode(
            val = root_val,
            left = self.buildTree(l_in, l_post),
            right = self.buildTree(r_in, r_post)
        )