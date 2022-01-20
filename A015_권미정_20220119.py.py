#A015
num = []
answer =0

num = list(map(int, input().split()))

for i in range(5):
    answer += (num[i])**2

answer = answer%10
print(answer)
