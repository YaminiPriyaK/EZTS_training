# BST

class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
def insertBST(root,value):
    if root == None:
        return node(value)
    if value < root.value:
        root.left = insertBST(root.left,value)
    if value > root.value:
        root.right = insertBST(root.right,value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
        
lst = [4,6,7,3,8,2,5,9,1]
root = node(lst.pop(0))

for i in lst:
    insertBST(root,i)
inorder(root)
