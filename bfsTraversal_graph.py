# graph
#bfs traversal

def bfs(dic,s):      # s-element 
    q = [s]
    v ={}
    for i in dic.keys():
        v[i] = False
    v[s] = True  
    while len(q) != 0:
        curr =q.pop(0)
        print(curr)
        for i in dic[curr]:
            if v[i[1]] == False:
                q.append(i[1])
                v[i[1]] = True
                    
                    
dic = {                           # adjacency list
    1:[(1,2,0),(1,3,0)],
    2:[(2,1,0),(2,7,0)],
    3:[(3,1,0),(3,6,0),(3,5,0)],
    4:[(4,7,0),(4,8,0)],
    5:[(5,3,0),(5,7,0)],
    6:[(6,3,0),(6,8,0)],
    7:[(7,2,0),(7,5,0),(7,4,0)],
    8:[(8,4,0),(8,6,0)]
}

visited = {
    1:False,          # visited
    2:False,
    3:False,
    4:False,
    5:False,
    6:False,
    7:False,
    8:False
}
    
bfs(dic,1)
