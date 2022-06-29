from collections import Counter, deque
from re import L

traffic = [deque() for _ in range(4)]
on_intersection = [1e+10 for _ in range(4)]
N = int(input())

for i in range(N):
    time, loc = input().split()
    time = int(time)

    if loc == 'A' : traffic[0].append([i,time])
    if loc == 'B' : traffic[1].append([i,time])
    if loc == 'C' : traffic[2].append([i,time])
    if loc == 'D' : traffic[3].append([i,time])

index = 0
while True:
    for i in range(4):
        if traffic[i]:
            if on_intersection[i] == 1e+10:
                on_intersection[i] = traffic[i].popleft()
            elif on_intersection[i] == traffic[i][0]:
                traffic[i][0] +=1

    prev_intersection = on_intersection.copy()

    if len(Counter(on_intersection)) == 1:
        if on_intersection[i] != 1e+10:
            for _ in range(4) : print(-1)
        
        break

    # right check
    for i in range(4):
        cursor_time = prev_intersection[i]
        right_time = prev_intersection[(i+3)%4]

        if cursor_time == 1e+10: continue
        if cursor_time == right_time:
            on_intersection[i] = prev_intersection[i] + 1

    min_time = min(on_intersection)

    prev_intersection = on_intersection.copy()

    print(prev_intersection)
    for i in range(4):
        if prev_intersection[i] == min_time and prev_intersection[i] != prev_intersection[(i+3)%4]:
            print(on_intersection[i])
            on_intersection[i] = 1e+10