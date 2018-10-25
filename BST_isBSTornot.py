'''
Author: Anitha Kiron Vedantam
Description: This is a program to check whether the given tree is a Binary Search Tree or not
'''


# Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Program to check BST
def checkBST(root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        minn = -float('inf')
        maxx = float('inf')
        return helper(root,minn,maxx)
        
def helper(node, minn, maxx):
    if node.data <= minn or node.data >= maxx:
        return False
    if not node.left and not node.right:
        return 
    if node.left:
        if helper(node.left,minn, node.data) == False:
            return False
    if node.right:
        if helper(node.right,node.data,maxx) == False:
            return False
        return True


if __name__ == '__main__':
        root = node(4)
        root.left = node(2)
        root.right = node(5)
        root.left.left = node(1)
        root.left.right = node(3)

        if checkBST(root):
                print("It is a Binary Search Tree")
        else:
                print("It is not a Binary Search Tree")
