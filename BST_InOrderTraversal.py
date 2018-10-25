'''
Author: Anitha Kiron Vedantam
Description: This is a program get the In-Order Traversal of a Binary Search Tree.
'''


# Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def InOrderTraversal(root):
        if not root:
            return 0
        InOrderTraversal(root.left)
        print(root.data)
        InOrderTraversal(root.right)
        return

if __name__ == '__main__':
        root = node(4)
        root.left = node(2)
        root.right = node(5)
        root.left.left = node(1)
        root.left.right = node(3)

        print("In-Order Traversal of Binary Search Tree:")
        InOrderTraversal(root)
