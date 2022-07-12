# BOJ 2667
# 단지번호붙이기

from collections import Counter, deque
from itertools import chain

N = int(input())

addr_map = [[] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
house_queue = deque()
stack = deque()

cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    row = input()
    for j in range(N):
        addr_map[i].append(int(row[j]))
        if row[j] == '1':
            house_queue.append([i,j])

while house_queue:
    cy, cx = house_queue.popleft()

    if not visited[cy][cx]:
        stack.append([cy, cx])
        cnt += 1

    while stack:
        y, x = stack.pop()

        addr_map[y][x] = cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= nx < N) and (0 <= ny < N) and (addr_map[ny][nx] != 0) and (not visited[ny][nx]):
                visited[ny][nx] = True
                stack.append([ny, nx])

counted = list(chain(*addr_map))
counted.append(0)
counted = Counter(counted)

sorted_counted = []

for i in range(1,len(counted)):
    sorted_counted.append(counted[i])

sorted_counted = sorted(sorted_counted)

print(len(counted)-1)

for d in sorted_counted:
    print(int(d))