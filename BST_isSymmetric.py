'''
Author: Anitha Kiron Vedantam
Description: This is a program check the symmetry of a BST
'''


# Node is defined as
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSymmetric(root):
    return(mirror(root,root))

def mirror(root1 , root2):
    # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
        return True

    if (root1 is not None and root2 is not None):
        if root1.data == root2.data:
            return (mirror(root1.left, root2.right)and mirror(root1.right, root2.left))
    return False


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    if isSymmetric(root) == True:
        print("It is a Symmetrical BST")
    else:
        print("It is not a Symmetrical BST")
