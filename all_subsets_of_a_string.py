s = input().strip()

l = list(s)
l.sort()

n = len(l)

arr = []
for i in range(2**n):
    temp = i
    t = ""
    for j in range(n):
        # t = ""
        if temp%2 == 1:
            # print(l[j],end="")
            t += l[j]       
        temp = temp >> 1
    arr.append(t)
# arr.sort()
print(arr)
        