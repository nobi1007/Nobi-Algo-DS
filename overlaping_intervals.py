a1 = [1,5]
a2 = [8,8]
a3 = [2,4]
# a4 = [8,9]
# a5 = [1,3]

l = [a1,a2,a3]
print(l)
l.sort()
print(l)
count = 0
current = l[0]
for i in range(len(l)-1):
    

    next = l[i+1]
    print(count,current,next)
    if min(current[1],next[0])<current[1]:
        current = [min(current[0],next[0]),max(current[1],next[1])]
    else:
        count += current[1] - current[0] + 1
        # print(current,count,"this")
        current = [next[0],next[1]]


    print(count,current,next)
    print()

count += current[1]-current[0] + 1
print(count)