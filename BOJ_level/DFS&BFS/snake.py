from collections import deque

N, M = map(int, input().split())
ladders = [list(map(int,input().split())) for _ in range(N)]
snakes = [list(map(int,input().split())) for _ in range(M)]
table = [0 for _ in range(101)]
queue = deque()

queue.append(1)

while queue:
    cursor = queue.popleft()

    for i in range(1, 7):
        new_cursor = cursor + i

        if new_cursor <= 100 and (table[new_cursor] == 0 or table[new_cursor] >= table[cursor]+1):

            for l in ladders :
                    if new_cursor == l[0]:
                        table[new_cursor] = table[cursor] + 1
                        table[l[1]] = table[cursor] + 1
                        queue.append(l[1])
                        break

            for s in snakes :
                    if new_cursor == s[0]:
                        table[new_cursor] = table[cursor] + 1
                        table[s[1]] = table[cursor]+1
                        queue.append(s[1])
                        break
       
            table[new_cursor] = table[cursor] + 1
            queue.append(new_cursor)

print(table[100])