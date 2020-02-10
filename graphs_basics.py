# from collections import defaultdict 
  
# class Graph: 

#     def __init__(self):   
#         self.graph = defaultdict(list) 
  
#     def addEdge(self, u, v): 
#         self.graph[u].append(v)
  
#     def DFSUtil(self, v, visited): 
  
#         visited[v] = True
#         print(v, end = ' ') 
  
#         # Recur for all the vertices  
#         # adjacent to this vertex 
#         for i in self.graph[v]: 
#             if visited[i] == False: 
#                 self.DFSUtil(i, visited) 
  
#     # The function to do DFS traversal. It uses 
#     # recursive DFSUtil() 
#     def DFS(self, v): 
#         visited = [False] * (len(self.graph)) 
#         self.DFSUtil(v, visited)




# g = Graph() 
# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(1, 2) 
# g.addEdge(2, 0) 
# g.addEdge(2, 3) 
# g.addEdge(3, 3)     


# print("Following is DFS from (starting from vertex 2)") 
# g.DFS(0)

import math

n = 8
mat = {}

mat[1] = [8]
mat[2] = []
mat[3] = [7]
mat[4] = [2]
mat[5] = [8]
mat[6] = [8]
mat[7] = [3]
mat[8] = [1,5,6]
# mat[9] = []
# mat[10] = []

# n = 4
# mat = {}
# mat[1] = [2,4]
# mat[2] = [1]
# mat[3] = []
# mat[4] = [1]


visited = [False for i in range(n+1)]

# def dfs(root,visited,l):

#     visited[root] = True
#     l.append(root)
#     # print(root)
#     for i in mat[root]:
#         if not visited[i]:
#             dfs(i,visited,l)
#     return (visited,l)

def dfs(root,visited,l):

    stack = []
    stack.append(root)
    # print(root)

    while len(stack):

        s = stack[-1]
        stack.pop()

        if not visited[s]:
            visited[s] = True
            l.append(s)

        for i in mat[s]:
            if not visited[i]:
                stack.append(i)
    return (visited,l)



count = 0
for i in range(1,len(visited)):
    if not visited[i]:
        l = []
        (visited,temp) = dfs(i,visited,l)
        print(temp)
        count += int(math.ceil(math.sqrt(len(temp))))
print(count)
# dfs(root,visited)