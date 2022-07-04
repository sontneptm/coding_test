# BOJ 7562
# 나이트의 이동

from collections import deque

N = int(input())

for _ in range(N):
    move = 0
    I = int(input())
    table = [[0 for _ in range(I)] for _ in range(I)]
    knight_stack = deque()
    start_loc = list(map(int, input().split()))
    target_loc = list(map(int, input().split()))

    knight_stack.append(start_loc)
    table[start_loc[0]][start_loc[1]] = -1

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    while knight_stack:
        y, x = knight_stack.popleft()
        if [y, x] is target_loc : break

        for i in range(8):
            if (0 <= y + dy[i] < I) and (0 <= x + dx[i] < I):
                ny = y + dy[i]
                nx = x + dx[i]

                if table[ny][nx] == 0:
                    table[ny][nx] = table[y][x] + 1
                    knight_stack.append([ny, nx])

    for t in table:
        move = max(*t, move)

    print("move:", move)