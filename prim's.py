# prim's algo

Graph = [
    [0,  7,  4, -1,  9],
    [7,  0,  6,  8, -1],
    [4,  6,  0, -1,  2],
    [-1, 8, -1,  0, -1],
    [9, -1,  2, -1,  0]
]

visited = [False] * len(Graph)
mini = float('inf')
x = y = -1
print(mini)
for i in range(len(Graph)):
    for j in range(len(Graph[i])):
        if Graph[i][j] == 0 or Graph[i][j] == -1:
            continue
        elif mini>Graph[i][j]:
            mini = Graph[i][j]
            x = i
            y = j
print(x+1,y+1,mini)

visited[x] = True
visited[y] = True
MST = []
MST.append(tuple((x+1,y+1,mini)))

while False in visited:
    mini = float('inf')
    for i in range(len(visited)):
        if visited[i] == True:           #
            for j in range(len(Graph[i])):
                if Graph[i][j] == 0 or Graph[i][j] == -1 or visited[j] == True:
                    continue
                elif mini>Graph[i][j]:
                    mini = Graph[i][j]
                    x = i
                    y = j
    visited[y] = True
    MST.append(tuple((x+1,y+1,mini)))
            
for i in MST:
    print(i)
