N = int(input())

seminars = []

for i in range(N):
    seminars.append(list(map(int,input().split())))

counter=0
last = -1 

seminars = sorted(seminars, key=lambda seminars: seminars[0])
seminars = sorted(seminars, key=lambda seminars: seminars[1])

for s in seminars:
    if s[0] >= last:
        last = s[1]
        counter +=1

print(counter)