#A033 나는 요리사다
score = [0]*5
sum = [0]*5
max=0
index = 0

for i in range(5):
    score[i] = list(map(int, input().split()))

for j in range(5):
    for k in range(4):
        sum[j] += score[j][k]
    if sum[j] > max:
        max = sum[j]
        index = j+1

print(index , max)




