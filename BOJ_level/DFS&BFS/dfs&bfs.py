# BOJ 1260
# DFS와 BFS

from collections import deque

N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
stack = deque()
queue = deque()

for _ in range(M):
    start, end = map(int,input().split())

    graph[start].append(end)
    graph[end].append(start)

def reverse_sorted(x) : return sorted(x, reverse=True)
graph = list(map(reverse_sorted,graph))

stack.append(V)
queue.append(V)

def dfs():
    while stack:
        cursor = stack.pop()
        if not visited[cursor]:
            visited[cursor] = True
            print(cursor, end=' ')
        
        for d in graph[cursor]:
            if not visited[d]:
                stack.append(d)

def bfs():
    while queue:
        cursor = queue.popleft()
        print(cursor, end=' ')

        for d in graph[cursor]:
            if not visited[d]:
                visited[d] = True
                queue.append(d)

dfs()
print()

visited = [False for _ in range(N+1)]
graph = list(map(sorted,graph))
visited[V] = True

bfs()
print()