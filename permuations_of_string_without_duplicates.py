from collections import deque
s = input()
l = deque([])
l.append(s)
n = len(s)
for i in range(n):
    count = 0
    level_q = deque([])
    while len(l)>0:
        x = l.popleft()
        for j in range(i,n):
            temp = list(x)
            if temp[i]!=temp[j] or i==j:
                (temp[i],temp[j]) = (temp[j],temp[i])
                level_q.append("".join(temp))
            print(i,j,l,level_q)
    for level in level_q:
        l.append(level)
print(l,len(l))

