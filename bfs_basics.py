# So in BFS two main topics are:
# 1- Level in a tree (this actually gives the minimum distance in case of unweighted graph)
# 2- minimum distance in a 0-1 weighted graph

# resource link : https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/


from collections import deque

# n = 8
# adjMat = {}
# adjMat[0] = [1,2,3]
# adjMat[1] = [0,4,5]
# adjMat[2] = [0,6,7]
# adjMat[3] = [0,7]
# adjMat[4] = [1]
# adjMat[5] = [1]
# adjMat[6] = [2]
# adjMat[7] = [2,3]


# n = 6
# adjMat = {}
# adjMat[0] = [1,2]
# adjMat[1] = [0,3]
# adjMat[2] = [0,3,4]
# adjMat[3] = [1,2,5]
# adjMat[4] = [2]
# adjMat[5] = [3]


n = 8
adjMat = {}
adjMat[0] = [1,2]
adjMat[1] = [0,3,4,5]
adjMat[2] = [0,6]
adjMat[3] = [1]
adjMat[4] = [1]
adjMat[5] = [1]
adjMat[6] = [2,7]
adjMat[7] = [6]



source = 0

visited = [0 for i in range(n)]
level = [0 for i in range(n)]       # For finding level of each layer in a tree or a graph (basic rule is that {{child's level = parent's level + 1}} )

visited[source] = 1
queue = deque([])

queue.append(source)
print(queue)
while len(queue)>0:
    current = queue.popleft()
    for i in adjMat[current]:
        if not visited[i]:
            queue.append(i)
            visited[i] = 1
            level[i] = level[current] + 1

            print(current,queue)
print(queue)

print("Levels",level)