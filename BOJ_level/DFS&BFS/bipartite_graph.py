# BOJ 1707
# 이분 그래프

from collections import deque

K = int(input())

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
stack = deque()

for _ in range(E):
    start, end = map(int, input().split())

    graph[start].append(end)
    graph[end].append(start)

stack.append(1)
visited[1] = 1

while stack:
    cursor = stack.pop() 
    
    for d in graph[cursor]:
        



