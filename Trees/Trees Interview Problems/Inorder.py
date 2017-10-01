class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder(tree):
    if not tree:
        inorder(tree.left)
        print tree.val
        inorder(tree.right)
        
