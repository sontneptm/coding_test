# BOJ 2178
# 미로 탐색

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
maze = [[0 for _ in range(M)] for _ in range(N)]
queue = deque()

for i in range(N):
    line = input()

    for j in range(len(line)):
        maze[i][j] = int(line[j])

queue.append([0,0])
maze[0][0] = 1

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0<= ny < N) and (0<= nx < M) and maze[ny][nx]==1:
            maze[ny][nx] = maze[y][x] + 1
            queue.append([ny, nx])

print(maze[N-1][M-1])
