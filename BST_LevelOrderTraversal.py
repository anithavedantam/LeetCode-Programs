'''
Author: Anitha Kiron Vedantam
Description: This is a program get the Level-Order Traversal of a Binary Search Tree.
'''


# Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LevelOrderTraversal(root):
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            level = []
            nextQueue = []
            for node in queue:
                level.append(node.data)
                if node.left: 
                    nextQueue.append(node.left)
                
                if node.right: 
                    nextQueue.append(node.right)
                
            queue = nextQueue
            res.append(level)
        return res

if __name__ == '__main__':
        root = node(4)
        root.left = node(2)
        root.right = node(5)
        root.left.left = node(1)
        root.left.right = node(3)

        print("Level Order Traversal of Binary Search Tree:")
        print(LevelOrderTraversal(root))

        
