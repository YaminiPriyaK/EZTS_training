# tree 
#postorder tree
class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None
        
def postorder(root):
    if root == None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.value)
        
if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    postorder(root)
