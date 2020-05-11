def matrix_mul_2(x,y):
    ans = [[0,0],[0,0]]
    ans[0][0] = x[0][0]*y[0][0] + x[0][1]*y[1][0]
    ans[0][1] = x[0][0]*y[0][1] + x[0][1]*y[1][1]
    ans[1][0] = x[1][0]*y[0][0] + x[1][1]*y[1][0]
    ans[1][1] = x[1][0]*y[0][1] + x[1][1]*y[1][1]
    return ans


n = 1
bin_n = bin(n-1)[2:]
arr = []
base = [[1,1],[1,0]]
arr.append(base)
for i in range(1,len(bin_n)):
    arr.append(matrix_mul_2(arr[i-1],arr[i-1]))
total = [[1,0],[0,1]]
I = total.copy()
for i in range(len(bin_n)):
    if bin_n[i] == '0':
        x = I.copy()
    else:
        x = arr[i]
    total = matrix_mul_2(total,x)
print(total[0][0]+total[0][1])
