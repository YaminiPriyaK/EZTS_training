# tree 
#preorder tree
class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None
        
def preorder(root):
    if root == None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)
        
if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    preorder(root)
