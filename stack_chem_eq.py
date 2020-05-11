# the aim of this code is to convert a given string "H2(OH)2" into this "H4O2" form.
from collections import deque

def separate(s):
    l = []
    i=0
    x = "0"
    while i<len(s):
        if not s[i].isnumeric():
            if int(x)!=0:
                l.append(int(x))
                x = "0"
            l.append(s[i])
        else:
            x += s[i]
        i += 1
    if x!="0":
        l.append(int(x))
    return l

s = input().strip()
stk = deque([])
dic = {}

arr = separate(s)

iter = 0
while iter < len(arr):
    if not arr[iter].isnumeric():
        stk.append(arr[iter])
        







