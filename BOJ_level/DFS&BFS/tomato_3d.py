# BOJ 7569
# 토마토

from collections import deque

M, N, H = map(int, input().split())
tomato_storage = [[[] for _ in range(N)] for _ in range(H)]
tomato_stack = deque()

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1]
days=-1

for i in range(H):
    for j in range(N):
        tomato_storage[i][j] = list(map(int,input().split()))
        for k in range(M):
            if tomato_storage[i][j][k] == 1: tomato_stack.append([i,j,k])

while tomato_stack:
    h, y, x = tomato_stack.popleft()

    for i in range(6):
        if (0 <= h+dh[i] < H) and (0 <= y+dy[i] < N) and (0 <= x+dx[i] < M):
            new_dest = [h+dh[i], y+dy[i], x+dx[i]]

            if tomato_storage[new_dest[0]][new_dest[1]][new_dest[2]] == 0:
                tomato_storage[new_dest[0]][new_dest[1]][new_dest[2]] = tomato_storage[h][y][x] + 1
                tomato_stack.append(new_dest)
                
for i in range(H):
    for j in range(N):
        if 0 in tomato_storage[i][j]:
            print(-1)
            exit()

        days = max(*tomato_storage[i][j], days)

print(days-1)

