import sys
from collections import deque

H, W = map(int,sys.stdin.readline().split())

image = list(map(int,sys.stdin.readline().split()))
visited = [[False for _ in range(W)] for _ in range(H)]
stack = deque()

dx = [-1,1,0,0]
dy = [0, 0,-1,1]

def q_function(start_point, target):
    visited[start_point[0]-1][start_point[1]-1] = True
    stack.append(start_point)

    while stack:
        cursor = stack.pop()
        x = cursor[0]-1
        y = cursor[1]-1

        for i in range(4):
            new_dest = [x + dx[i] , y + dy[i]]

            if new_dest[0] <= 0 or new_dest[0] >= H: continue
            if new_dest[1] <= 0 or new_dest[1] >= W: continue
        
            if image[new_dest[0]][new_dest[1]] == image[x][y]:
                visited[new_dest[0]][new_dest[1]] = True
                stack.append(new_dest)

    for i in range(H):
        for j in range(W):
            if visited[i][j]: 
                print("i",type(target))
                print("i",j)
                print("img", image)
                image[i][j] = target

Q = int(sys.stdin.readline())

for _ in range(Q):
    x, y, t = list(map(int,sys.stdin.readline().split()))
    q_function([x,y], t)

print(image)
