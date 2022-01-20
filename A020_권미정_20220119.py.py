#A020

people =[list(map(int, input().split())) for _ in range(4)]

people_num = 0
max = 0

for i in range(4):
    people_num -= people[i][0]
    people_num += people[i][1]
    if people_num > max:
        max = people_num

print(max)