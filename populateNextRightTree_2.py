"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # Init leftmost
        leftmost = root

        # Go through level by level
        while leftmost:

            head = leftmost

            # While traversing one level
            while head:

                # Handling head.left.next
                # Case 1 (2 children)
                if head.left and head.right:
                    head.left.next = head.right

                # Case 2 (1 child)
                elif head.left and not head.right:

                    # Find next element for head.left.next
                    next_node = head.next

                    while next_node and not head.left.next:

                        # Try both
                        if next_node.left:
                            head.left.next = next_node.left

                        elif next_node.right:
                            head.left.next = next_node.right

                        # If none, keep moving
                        next_node = next_node.next


                # Handle head.right.next
                if head.right:

                    next_node = head.next

                    while next_node and not head.right.next:

                        # Try both
                        if next_node.left:
                            head.right.next = next_node.left

                        elif next_node.right:
                            head.right.next = next_node.right

                        # If none, keep moving
                        next_node = next_node.next



                # Move head along
                head = head.next

            # Move to next level
            if leftmost.left:
                leftmost = leftmost.left
            else:
                leftmost = leftmost.right

        return root