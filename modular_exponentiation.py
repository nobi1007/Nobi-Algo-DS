### NAIVE APPROACH

# def power(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x,n-1)

# def power(x,n):
#     tot = 1
#     for i in range(n):
#         tot *= x
#     return(tot)

# print(power(2,3))


### BINARY EXPONENTIATION

# def power(x,n):
#     if n == 0:
#         return 1
#     if n%2 == 0:
#         return power(x*x,n//2)
#     else:
#         return x * power(x*x,(n-1)//2) 

def power(x,n,m):
    tot = 1
    while n>0:
        if n%2 == 1:
            tot = (tot * x)%m
        x = (x * x)%m
        n //= 2
    return tot
print(power(3,100000000000000,10**9+7))