stones = int(input())

height_list = list(map(int, input().split()))

counter = 1
largest = height_list[0]

for h in height_list:
    if largest < h:
        largest = h
        counter +=1

print(counter)