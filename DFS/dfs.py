from collections import deque

N,M,R = map(int,input().split())

stack = deque()
graph = [[] for _ in range(N+1)]
visited_with_order = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def reverse_sorted(l): return list(reversed(sorted(l)))
graph = list(map(reverse_sorted, graph))

stack.append(R)
order = 1

while stack:
    cursor = stack.pop()

    if visited_with_order[cursor] == 0:
        visited_with_order[cursor] = order
        order +=1

    for g in graph[cursor]:
        if visited_with_order[g] == 0:
            stack.append(g)

for i in range(1, N+1):
    print(visited_with_order[i])