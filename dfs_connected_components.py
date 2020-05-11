n,edges = list(map(int,input().split()))
visited = [0 for i in range(n)]
mat = {}
for i in range(edges):
    x,y = list(map(int,input().split()))
    if x in mat:
        mat[x].append(y)
    else:
        mat[x] = [y]
    
    # for Unidirected Graph
    if y in mat:
        mat[y].append(x)
    else:
        mat[y] = [x]
count = 1
# print(mat)
for node in range(1,n+1):
    if visited[node-1] != 0:
        continue
    stack = []
    stack.append(node)
    visited[node-1] = count
    while len(stack):
        curr = stack.pop()
        # print(node,curr)
        if curr in mat:
            for child in mat[curr]:
                if visited[child-1]==0:
                    stack.append(child)
                    visited[child-1] = count
    count += 1
print(visited)


# input 1:
# 
# 3 3
# 1 2
# 1 3
# 2 3

