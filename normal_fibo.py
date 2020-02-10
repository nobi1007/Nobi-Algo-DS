def fibo2(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return fibo2(num-1)+fibo2(num-2)
