# BOJ 24444 & 24445
# 알고리즘 수업 - 너비 우선 탐색 1 & 알고리즘 수업 - 너비 우선 탐색 2

from collections import deque

N, M, R = map(int, input().split())

queue = deque()
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

def reverse_sorted(l): return list(reversed(sorted(l)))
graph = list(map(reverse_sorted, graph))

queue.append(R)
visited[R] = 1
order=2

while queue:
    cursor = queue.popleft()

    for node in graph[cursor]:
        if visited[node] == 0:
            visited[node] = order
            order +=1
            queue.append(node)

for i in range(1, N+1):
    print(visited[i])