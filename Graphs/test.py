n=int(input())
a=int(input())
b=int(input())
c=0
print(a)
print(b)
for i in range (2,n):
    c=a+b
    a=b
    b=c
    print(c)