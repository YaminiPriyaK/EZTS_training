#tree
# level order

class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None
        
def levelorder(root):
    Q = [root]
    Q.append(None)
    
    while len(Q) > 0:
        curr = Q.pop(0)
        if curr == None:
            if len(Q) == 0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(curr.value, end =" ")
            if curr.left != None:
                Q.append(curr.left)
            if curr.right != None:
                Q.append(curr.right)
                
def height(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return max(lh,rh)+1

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right.right.right = Node(11)
    root.left.right.right.left = Node(12)
    root.left.right.right.right = Node(13)
    
    levelorder(root)
    print()
    hi = height(root)
    print("The height of the tree is: ",hi)
