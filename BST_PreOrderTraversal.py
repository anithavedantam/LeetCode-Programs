'''
Author: Anitha Kiron Vedantam
Description: This is a program get the Pre-Order Traversal of a Binary Search Tree.
'''


# Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PreOrderTraversal(root):
        if not root:
            return 0
        print(root.data)
        PreOrderTraversal(root.left)
        PreOrderTraversal(root.right)
        return

if __name__ == '__main__':
        root = node(4)
        root.left = node(2)
        root.right = node(5)
        root.left.left = node(1)
        root.left.right = node(3)

        print("Pre-Order Traversal of Binary Search Tree:")
        PreOrderTraversal(root)
