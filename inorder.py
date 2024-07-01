# tree 
#inorder tree
class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None
        
def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.value)
    inorder(root.right)
        
if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    inorder(root)
