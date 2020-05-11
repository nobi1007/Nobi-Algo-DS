from math import sqrt
prime = []
main_prime = []

def simple_sieve(l,r):
    temp = [True for i in range(r)]
    temp[0],temp[1] = False,False
    p = 2
    while p*p<=r:
        if temp[p]:
            for i in range(p*p,r,p):
                temp[i] = False
        p += 1
        
    for i in range(len(temp)):
        if temp[i]:
            prime.append(i)
            if i>=l:
                main_prime.append(i)

def solve(n, m):
    limit = int(sqrt(m)) + 1
    simple_sieve(n,m)

    low = limit
    high = limit*2

    while low<m:
        if high>=m:
            high = m

        mark = [True for i in range(limit+2)]
        for i in range(len(prime)):
            
            low_lim = (low//prime[i]) * prime[i]
            if low_lim<low:
                low_lim += prime[i]

            for j in range(low_lim,high+1,prime[i]):
                mark[j-low] = False
        
        for i in range(low,high+1):
            if mark[i-low]:
                if i>=n and i<=m:
                    main_prime.append(i)
        low += limit
        high += limit
    count = 0
    for i in range(1,len(main_prime)):
        if main_prime[i]-main_prime[i-1] == 2:
            count += 1
    return count

print(solve(10,1000000))