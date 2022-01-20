#A022 핸드폰 요금
'''
30초보다 작으면 영식이 이득
30초 - 60초 사이면 민식이 이득
1분
'''

N = int(input())#통화개수
Y=0
M=0

hour = list(map(int,input().split()))

for i in range(N):
    Y += ((hour[i]//30)+1)*10
    M += ((hour[i]//60)+1)*15

if Y > M:
    print ('M',M)
elif M > Y:
    print('Y', Y)
else :
    print('Y M',Y)