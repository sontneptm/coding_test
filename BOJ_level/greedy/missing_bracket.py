#BOJ 1541
# 잃어버린 괄호

exp_str = input()

rtn = 0

exp_str = exp_str.split('-')

for i in range(len(exp_str)):
    s = exp_str[i]
    p = s.split("+")
    p = list(map(int,p))
    p_sum = sum(p)

    if i != 0:
        rtn-=p_sum
    else:
        rtn+=p_sum

print(rtn)