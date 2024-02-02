from typing import List, Dict
import math

class Node:

    def __init__(self, value):

        self.value = value
        self.right = None
        self.left = None

    def to_dict(self) -> Dict:
        pass

class InvalidTreeError(Exception):
    pass

def create_binary_tree(array: List[int]) -> Node:
    if not array:
        return -1
    
    root = Node(array[0])
    queue = [root]
    i = 1

    while i < len(array) and queue:
        # Leaf node, skip
        if array[i] == -1 and array[(i - 1) // 2] == -1:
            i += 1
        # Orphaned node, error
        elif array[i] != -1 and array[(i - 1) // 2] == -1:
            raise InvalidTreeError
        else:
            current_node = queue.pop(0)

            # Add left child
            if i < len(array) and array[i] != -1:
                current_node.left = Node(array[i])
                queue.append(current_node.left)
            i += 1

            # Add right child
            if i < len(array) and array[i] != -1:
                current_node.right = Node(array[i])
                queue.append(current_node.right)
            i += 1

    if i < len(array):
        raise InvalidTreeError

    return root

def generate_permutations(node: Node) -> List[Node]:
    pass



def print_tree(node, depth=0, prefix="Root:"):
    if node:
        print("  " * depth + f"{prefix} {node.value}")
        print_tree(node.left, depth + 1, "L:")
        print_tree(node.right, depth + 1, "R:")

x = create_binary_tree([1, 2, 3, 4, -1, 5, -1, -1, 6, -1, -1, 7, 3, -1, -1, -1, -1, 1])


print_tree(x)