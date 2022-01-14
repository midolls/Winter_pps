'''
A008
일단 테스트 케이스 수 만큼 INPUT을 반복할거임
INPUT한줄을 해서 SPLIT해서 나누고 처음 수는 모두 학생의 수라는 것을 아니까 줄마다 첫번째수만틈 뒤에거를 다더해서 학생수만큼 나눠서 평균구하기,,,
그리고 나서 학생수만큼 반복문 해서 평균이랑 비교

'''

C = int(input())
mylist = [0 for _ in range(C)]
sumlist = []
average = []
sum=0
num=0

for i in range(C):
    mylist[i] = list(map(int,input().split()))

for i in range(C):
    k = mylist[i][0]
    for j in range(1,k+1):
        sum = sum + mylist[i][j]
    average.append(sum/k)
    sum=0

for i in range(C):
    for j in range(mylist[i][0]):
        if mylist[i][j+1] > average[i]:
            num+=1
    print(format((num/mylist[i][0]),"5.3%"))
    num=0