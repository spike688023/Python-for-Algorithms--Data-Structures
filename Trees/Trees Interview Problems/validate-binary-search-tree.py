#Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Morris Traversal Solution
class Solution:
    def inorder(self, root):
        list1 = []
        if root.left == None:
            return root.val
        else:
            #print "left tree"
            list1.append( self.inorder(root.left) )
            #print "middle"
            list1.append( root.val )
            #print "right tree"
            list1.append( self.inorder(root.right) )
            return list1
        
    def isValidBST(self, root):
        list1 = self.inorder(root)  
        #for i in list1: print i
        if len(list1) <= 1: return True
        else:
            for i in range(1,len(list1)): 
                if list1[i] < list1[i - 1] : return False
        return True
                    
            

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print Solution().isValidBST(root)
    #print Solution().inorder(root)
