storage = {0:1,1:1}
def fibo(num):
    if num == 0:
        return storage[0]
    elif num == 1:
        return storage[1]
    else:
        try:
            storage[num] = storage[num-1] + storage[num-2]
            return storage[num]
        except KeyError:
            storage[num] = fibo(num-1) + fibo(num-2)  
            return storage[num]