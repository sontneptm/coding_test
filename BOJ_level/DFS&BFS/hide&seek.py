# BOJ 1697
# 숨바꼭질

from calendar import c
from collections import deque

N, K = map(int,input().split())
visited = [0 for _ in range(100001)]

queue = deque()
queue.append(N)

def bfs():
    while queue:
        cursor = queue.popleft()
        if cursor == K : return visited[cursor]

        for nd in (cursor-1, cursor+1, 2*cursor):
            if (0 <= nd <= 100000) and (visited[nd] == 0) :
                visited[nd] = visited[cursor] + 1
                queue.append(nd)

                if nd == K: return visited[nd]
            
print(bfs())