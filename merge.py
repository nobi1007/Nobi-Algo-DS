def merge(a1,a2):
    n = len(a1)
    m = len(a2)
    i,j = (0,0)
    arr = []
    arr_pos = []
    while i+j < n+m:
        if i == n:
            arr.append(a2[j])
            arr_pos.append(2)
            j += 1
        elif j == m:
            arr.append(a1[i])
            arr_pos.append(1)
            i += 1
        elif a1[i] < a2[j]:
            arr.append(a1[i])
            arr_pos.append(1)
            i += 1
        elif a1[i] >= a2[j]:
            arr.append(a2[j])
            arr_pos.append(2)
            j += 1
    print(a1)
    print(a2)
    print(arr_pos)
    return arr