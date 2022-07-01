# BOJ 2606
from collections import deque
from collections import Counter

stack = deque()
com_num = int(input())
conn_num = int(input())

graph = [[] for _ in range(com_num+1)]
visited = [False for _ in range(com_num+1)]

for _ in range(conn_num):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited[1] = True
stack.append(1)

while stack:
    cursor = stack.pop()

    for n in graph[cursor]:
        if not visited[n]:
            visited[n] = True
            stack.append(n)

print(Counter(visited)[True]-1)
