dp = {}

edges = [
    [1,2],
    [1,3],
    [1,4],
    [2,5],
    [2,6],
    [3,7],
    [4,8],
    [4,9],
    [4,10],
    [5,11],
    [5,12],
    [7,13],
    [7,14] 
]

mat = {}

for i in edges:
    x,y = i
    if x in mat:
        mat[x].append(y)
    else:
        mat[x] = [y]
    if y in mat:
        mat[y].append(x)
    else:
        mat[y] = [x]
    
values = [
    3,
    2,
    1,
    10,
    1,
    3,
    9,
    1,
    5,
    3,
    4,
    5,
    9,
    8
]

dp = {}

def dfs(values,curr,parent):
    dp[curr] = values[curr-1]
    maxi = 0
    for child in mat[curr]:
        if child == parent:
            continue
        dfs(values,child,curr)
        maxi = max(maxi,dp[child])
    dp[curr] += maxi
dfs(values,1,0)
print(dp[1])