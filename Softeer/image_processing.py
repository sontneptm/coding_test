import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())

image = []

for _ in range(H):
    image.append(list(map(int, sys.stdin.readline().split())))

Q = int(sys.stdin.readline())

dx = [-1,1,0,0]
dy = [0, 0,-1,1]

def q_function(start_point, target):
    visited = [[False for _ in range(W)] for _ in range(H)]
    stack = deque()
    visited[start_point[0]-1][start_point[1]-1] = True
    start_point = [start_point[0]-1,start_point[1]-1]
    stack.append(start_point)

    while stack:
        cursor = stack.pop()
        x = cursor[0]
        y = cursor[1]

        for i in range(4):
            new_dest = [x + dx[i] , y + dy[i]]


            if new_dest[0] < 0 or new_dest[0] >= H: 
                continue
            if new_dest[1] < 0 or new_dest[1] >= W: 
                continue
        
            if image[new_dest[0]][new_dest[1]] == image[x][y] and not visited[new_dest[0]][new_dest[1]]:
                visited[new_dest[0]][new_dest[1]] = True
                stack.append(new_dest)

    for i in range(H):
        for j in range(W):
            if visited[i][j]: 
                image[i][j] = target

for _ in range(Q):
    x, y, t = list(map(int,input().split()))
    q_function([x,y], t)

for i in range(len(image)):
    print(*image[i])

