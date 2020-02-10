mat = []
n = 50
char = '.'
l = [[char for i in range(n)] for j in range(n)]
for i in l:
    for j in i:
        print(j,end=" ")
    print()