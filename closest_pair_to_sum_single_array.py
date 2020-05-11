arr = list(map(int,input().split()))
x = int(input())
left = 0
right = len(arr) - 1
I = 0
J = 0
mini = 10**5+10
while left<right:
    if abs(arr[left]+arr[right]-x) < mini:
        mini = abs(arr[left]+arr[right]-x)
        I = arr[left]
        J = arr[right]
    if arr[left]+arr[right] > x:
        right -= 1
    else:
        left += 1
print([I,J,mini])