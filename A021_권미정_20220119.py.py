#A021 플러그
'''
일단 플러그수만큼 뭔갈 연결할 수 있는데 여기서 연결하느라 쓴 한개씩을 줘야해서 마지막에 연결안한 멀티탭빼고 멀티탭개수-1만큼 빼줘야함
'''
import sys
input = sys.stdin.readline

N = int(input())
sum =0

for _ in range(N):
    sum += int(input())

print (sum-(N-1))
