n = int(input())

board = [[0 for i in range(n)] for j in range(n)]

def is_attacked(board,i,j):
    for x in range(len(board)):
        if board[i][x] == 1:
            return True
    
    for x in range(len(board)):
        if board[x][j] == 1:
            return True
    
    for x in range(len(board)):
        for y in range(len(board)):
            if x+y == i+j:
                if board[x][y] == 1:
                    return True
    
            if x-y == i-j:
                if board[x][y] == 1:
                    return True
    return False
        

def n_queens(n):
    global board
    if n == 0:
        return True
    N = len(board)
    for i in range(N):
        for j in range(N):
            # print(i,j,board)
            if is_attacked(board,i,j):
                continue
            board[i][j] = 1
            if n_queens(n-1):
                return True
            board[i][j] = 0
    return False

count = 0
arr = []
# for i in range(n):
if n_queens(n):
    # arr.append(board.copy())
    count += 1
if count > 0:
    print("YES")
    # for i in arr:
    for j in board:
        for k in j:
            print(k,end=" ")
        print()
        # print()
        # print()
else:
    print("NO")