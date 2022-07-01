# BOJ 1012
# 유기농 배추
from collections import deque

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    M, N, K = map(int,input().split())
    cab_field = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[0 for _ in range(N)] for _ in range(M)]
    cab_loc = []
    cab_stack = deque()
    counter = 0

    for _ in range(K):
        X,Y = map(int,input().split())
        cab_field[X][Y] = 1
        cab_loc.append([X,Y])

    def dfs(start_loc):
        cab_stack.append(start_loc)

        while cab_stack:
            cursor = cab_stack.pop()
            x = cursor[0]
            y = cursor[1]
            visited[x][y] = 1

            for i in range(4):
                if x+dx[i] < 0 or x+dx[i] >= M: continue
                if y+dy[i] < 0 or y+dy[i] >= N: continue
                new_dest = [x+dx[i], y+dy[i]]

                if (cab_field[new_dest[0]][new_dest[1]] == 1) and (visited[new_dest[0]][new_dest[1]]!= 1) :
                    cab_stack.append(new_dest)

    for loc in cab_loc:
        if visited[loc[0]][loc[1]] != 1:
            counter+=1
            dfs(loc)

    print(counter)










    

    
    
    