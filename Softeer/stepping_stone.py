import sys

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if H[i] > H[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
