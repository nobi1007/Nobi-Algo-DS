from collections import deque
from sys import maxsize as MAX

# n = 5
# adjMat = {}
# adjMat[0] = [(1,1),(2,1),(3,0)]
# adjMat[1] = [(0,1),(4,0)]
# adjMat[2] = [(0,1),(3,0)]
# adjMat[3] = [(0,0),(2,0),(4,0)]
# adjMat[4] = [(1,0),(3,0)]

n = 9
adjMat = {}
adjMat[0] = [(1,0),(7,1)]
adjMat[1] = [(0,0),(7,1),(2,1)]
adjMat[2] = [(1,1),(3,0),(5,0),(8,1)]
adjMat[3] = [(2,0),(4,1),(5,1)]
adjMat[4] = [(3,1),(5,1)]
adjMat[5] = [(2,0),(3,1),(4,1),(6,1)]
adjMat[6] = [(5,1),(7,1),(8,1)]
adjMat[7] = [(0,1),(1,1),(6,1),(8,1)]
adjMat[8] = [(2,1),(6,1),(7,1)]


Q = deque([])
distance = [MAX for i in range(n)]

source = 0
distance[source] = 0

Q.append(source)

while len(Q)>0:
    
    v = Q.popleft()

    for i in adjMat[v]:
        if distance[i[0]] > distance[v] + i[1]:
            distance[i[0]] = distance[v] + i[1]

            # if i[1] == 0:
            #     Q.appendleft(i[0])
            # else:
            Q.append(i[0])
            # Here the doubt is : why to use a doubley ended queue here??

print(distance)
        