# BOJ 16928
# 뱀과 사다리 게임

from collections import deque

N, M = map(int, input().split())
ladders = [list(map(int,input().split())) for _ in range(N)]
snakes = [list(map(int,input().split())) for _ in range(M)]
visited = [0 for _ in range(101)]
graph = [[] for _ in range(101)]
queue = deque()

for i in range(1,100):
    for j in range(1,7):
        if i+j <= 100:
            checker = True
            for l in ladders:
                if l[0] == i+j:
                    graph[i].append(l[1])
                    checker = False

            for s in snakes:
                if s[0] == i+j:
                    graph[i].append(s[1])
                    checker = False

            if checker:
                graph[i].append(i+j)

queue.append(1)

while queue:
    cursor = queue.popleft()

    for d in graph[cursor]:
        if visited[d] == 0:
            visited[d] = visited[cursor]+1
            queue.append(d)

print(visited)