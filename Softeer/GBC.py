N, M = map(int,input().split())

limit_list = [0 for _ in range(100)]
real_list = [0 for _ in range(100)]
last = 0

for _ in range(N):
    length, limit = map(int, input().split())
    limit_list[last:last+length] = [limit for _ in range(length)]
    last += length

last = 0

for _ in range(M):
    length, real = map(int, input().split())
    real_list[last:last+length] = [real for _ in range(length)]
    last += length


def sub(a,b):
    return a-b

diff = list(map(sub, real_list, limit_list))

max_diff = max(diff)

print(max_diff if max_diff>=0 else 0)
