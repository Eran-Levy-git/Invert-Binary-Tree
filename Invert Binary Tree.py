from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invert_tree(root.right)
            self.invert_tree(root.left)
            root.left, root.right = root.right, root.left
        return root


class Auxiliary:
    def get_height(self, node):
        if not node:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right)) + 1

    def print_tree(self, node, prefix="", is_left_child=True):
        if not node:
            return
        if node.right:
            self.print_tree(
                node.right, prefix + ("   " if is_left_child else "    "), False
            )
        connector = "└── " if is_left_child else "┌── "
        print(prefix + (connector if prefix else "   ") + str(node.val))
        if node.left:
            self.print_tree(
                node.left, prefix + ("    " if is_left_child else "   "), True
            )

    def build_binary_tree(self, values, index=0):
        if index >= len(values) or values[index] is None:
            return None

        node = TreeNode(values[index])
        node.left = self.build_binary_tree(values, 2 * index + 1)
        node.right = self.build_binary_tree(values, 2 * index + 2)
        return node


"""
Example of usage:
"""

# Level-order traversal list
tree_values = [4, 2, 7, 1, 3, 6, 9]

# Create the binary tree
aux = Auxiliary()
root = aux.build_binary_tree(tree_values)

print("\nOriginal Tree:\n")
aux.print_tree(root)

print("\nInverted Tree:\n")

sol = Solution()
root = sol.invert_tree(root)
aux.print_tree(root)

print()
