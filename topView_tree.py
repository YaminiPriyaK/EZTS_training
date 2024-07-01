#top view

class node_data:
    def __init__(self,Node,HKey):
        self.Node = Node
        self.HKey = HKey

def topview(root):
    temp = node_data(root,0)
    Q = [temp]
    Q.append(None)
    
    key_dict = {}
    
    while len(Q) != 0:
        curr = Q.pop(0)
        
        if curr == None:
            if len(Q) == 0:
                break
            else:
                Q.append(None)
        else:
            if curr.HKey not in key_dict.keys():
                key_dict[curr.HKey] = curr.Node.value
            if curr.Node.left != None:
                temp = node_data(curr.Node.left,curr.HKey-1)
                Q.append(temp)
            if curr.Node.right != None:
                temp = node_data(curr.Node.right,curr.HKey+1)
                Q.append(temp)
    for i in sorted(key_dict):
        print(key_dict[i])
    print(key_dict)
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
    
    topview(root)
