
def merge(st1,st2):
    l = []
    i,j,n,m = 0,0,len(st1),len(st2)
    while i+j<m+n:
        if i==n:
            l.append(st2[j])
            j += 1
        elif j==m:
            l.append(st1[i])
            i += 1
        elif st1[i]<=st2[j]:
            l.append(st1[i])
            i += 1
        elif st1[i]>st2[j]:
            l.append(st2[j])
            j += 1
    return l

def mergeSort(arr):
    n = len(arr)
    if n==0:
        return []
    elif n==1:
        return arr
    else:
        left = 0
        right = n
        mid = n//2
        lhalf = arr[left:mid]
        rhalf = arr[mid:right]
        half1 = mergeSort(lhalf)
        half2 = mergeSort(rhalf)
        return(merge(half1,half2))

#n = 1000000
#l = [i for i in range(n,-1,-1)]
#l2 = mergeSort(l)

