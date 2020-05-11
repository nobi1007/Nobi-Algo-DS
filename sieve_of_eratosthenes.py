n = int(input())
prime = [False,False]
for i in range(2,n):
    prime.append(True)

p = 2
while p*p <= n:
    if prime[p] == True:
        for i in range(p*p,n,p):
            if prime[i] == True:
                prime[i] = False
                print(p,i)
    p += 1

l = []
for i in range(n):
    if prime[i]:
        l.append(i)
print(l)