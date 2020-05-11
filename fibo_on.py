n = int(input())
first = 1
second = 1
for i in range(2,n+1):
    (second,first) = (second+first,second)
print(second)
     