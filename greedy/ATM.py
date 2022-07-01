N = int(input())
time_list = sorted(list(map(int, input().split())))

for i in range(1, N):
    time_list[i] += time_list[i-1]

print(sum(time_list))