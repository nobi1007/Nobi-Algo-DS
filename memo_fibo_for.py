storage = {0:1,1:1}
def ffibo(num):
    try:
        storage[num] = storage[num-1]+storage[num-2]
        return(storage[num])
    except KeyError:
        x = max(list(storage))
        print(x)
        for i in range(x+1,num+1):
            storage[i] = storage[i-2]+storage[i-1]
        return storage[num]