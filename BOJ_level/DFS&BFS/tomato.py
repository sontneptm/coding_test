# BOJ 7576 
# 토마토
from collections import deque

M, N = map(int, input().split())

tomato_storage = []
tomato_queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
days = -1

for i in range(N):
    tomato_storage.append(list(map(int, input().split())))
    for j in range(M):
        if tomato_storage[i][j] == 1 : tomato_queue.append([i,j])

while tomato_queue:
    y,x = tomato_queue.popleft()

    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M : 
            new_dest = [y+dy[i], x+dx[i]]

            if tomato_storage[new_dest[0]][new_dest[1]]==0:
                tomato_storage[new_dest[0]][new_dest[1]] = tomato_storage[y][x] + 1
                tomato_queue.append(new_dest)

for t in tomato_storage:
    if (0 in t):
        print(-1)
        exit(0)
    days = max(*t, days)

print(days-1)