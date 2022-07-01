# BOJ 13305
# 주유소

N = int(input())
distance_list = list(map(int, input().split()))
value_list = list(map(int, input().split()))

min_val = min(value_list)

total = 0
prev_val = value_list[0]
prev_idx = 0

for i in range(N):  
    if prev_val == min_val:
        total += prev_val * (sum(distance_list[prev_idx:N]))
        break
    elif value_list[i] < prev_val:
        total += prev_val * (sum(distance_list[prev_idx:i]))
        prev_val = value_list[i]
        prev_idx = i

print(total)