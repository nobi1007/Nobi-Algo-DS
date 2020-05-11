arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
x = int(input())
n1 = len(arr1)
n2 = len(arr2)
i = 0
j = n2-1
mini = 10**5+10
I = 0
J = 0
while i<n1 and j>=0:
    if abs(arr1[i]+arr2[j]-x) <= mini:
        mini = abs(arr1[i]+arr2[j]-x)
        I = arr1[i]
        J = arr2[j]
    
    if arr1[i]+arr2[j] > x:
        j -= 1
    else:
        i += 1
    
print([mini,I,J])
