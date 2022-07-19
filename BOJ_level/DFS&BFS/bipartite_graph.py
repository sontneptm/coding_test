# BOJ 1707
# 이분 그래프

from collections import deque

def bfs():
    while queue:
        cursor = queue.popleft()

        for g in graph[cursor]:
            if visited[g] == 0:
                visited[g] = visited[cursor] * -1
                queue.append(g)
            elif visited[g] == visited[cursor]:
                return False
    return True
    
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    queue = deque()
    is_bipartite = True

    for _ in range(E):
        start, end = map(int, input().split())

        graph[start].append(end)
        graph[end].append(start)

    for i in range(1, V+1):
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1
            is_bipartite = bfs()

        if not is_bipartite: break

    print("YES" if is_bipartite else "NO")