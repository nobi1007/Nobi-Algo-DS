n = int(input())
arr = list(map(int,input().split()))

x = int(input())
dic = {}

for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1 

count = 0

for i in dic:
    if x-i in dic:
        count += dic[i]
    if x-i == i:
        count -= 1
        
print(count)

# for i in dic:
#     if abs(i-x) in dic:
#         count += dic[i]
#     if abs(i+x) in dic:
#         count += dic[i]
    


# print(dic)
# print(count//2)