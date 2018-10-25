'''
Author: Anitha Kiron Vedantam
Description: This is a program to find the maximum depth of the Binary Search Tree
'''

# Definition for a binary tree node.
class node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    if root == None:
        return 0
    return max(maxDepth(root.left),maxDepth(root.right)) + 1

if __name__ == '__main__':
        root = node(4)
        root.left = node(2)
        root.right = node(5)
        root.left.left = node(1)
        root.left.right = node(3)

        print("Height of tree is %d" %(maxDepth(root)))

