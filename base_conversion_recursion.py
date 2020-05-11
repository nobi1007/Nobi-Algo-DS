n,b = map(int,input().split())
hm = {}
for i in range(10):
    hm[i] = str(i)
hm[10] = "A"
hm[11] = "B"
hm[12] = "C"
hm[13] = "D"
hm[14] = "E"
hm[15] = "F"

def convert(n,b):
    if n<b:
        print(hm[n],end="")
        return 0
    convert(n//b,b)
    print(hm[n%b],end="")

convert(n,b)
print()
    