# BOJ 11047
# 동전0

N, K = map(int, input().split())

values = []
counter = 0

for i in range(N):
    values.append(int(input()))

for d in reversed(values):
    if d>K : continue

    counter += K//d
    K = K%d

print(counter)