# BOJ 7562
# 나이트의 이동

from collections import deque

N = int(input())

for _ in range(N):
    I = int(input())
    table = [[0 for _ in range(I)] for _ in range(I)]
    knight_queue = deque()
    start_loc = list(map(int, input().split()))
    target_loc = list(map(int, input().split()))

    knight_queue.append(start_loc)

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    def bfs():
        while knight_queue:
            y, x = knight_queue.popleft()
            if [y,x] == target_loc : return 0

            for i in range(8):
                if (0 <= y + dy[i] < I) and (0 <= x + dx[i] < I):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if table[ny][nx] == 0:
                        table[ny][nx] = table[y][x] + 1
                        if [ny, nx] == target_loc:
                            return table[ny][nx]
                        knight_queue.append([ny, nx])

    print(bfs())