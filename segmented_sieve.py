from math import sqrt
prime = []

def simple_sieve(l,n):
    temp = [True for i in range(n)]
    temp[0],temp[1] = False,False
    p = 2
    while p*p<=n:
        if temp[p]:
            i = p*p
            while i<n:
                temp[i] = False
                i += p
        p += 1

    for i in range(len(temp)):
        if temp[i]:
            if i >= l:
                print(i,end = " ")
            prime.append(i)

def segmented_sieve(l,n):
    limit = int(sqrt(n)) + 1
    simple_sieve(l,limit)
    low = limit
    high = limit*2
    
    while low<n:
        
        if high >= n:
            high = n
        
        mark = [True for _ in range(limit+2)]        
        
        for i in range(len(prime)):
        
            low_lim = (low//prime[i]) * prime[i]
            if low_lim<low:
                low_lim += prime[i]
        
            for j in range(low_lim,high+1,prime[i]):
                mark[j-low] = False
        
        for i in range(low,high+1):
            if mark[i-low]:
                if i>=l and i<=n:
                    print(i,end= " ")
        low += limit
        high += limit


l,r = list(map(int,input().split()))
segmented_sieve(l,r)
print()