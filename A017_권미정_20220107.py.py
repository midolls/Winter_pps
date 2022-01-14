'''
A017
0~9까지의 리스트를 만들어서 필요한 세트 개수를 리스트에 담을거임

다른숫자들은 개수만큼 구매하면 되고
6이나 9가 나오면 일단 둘다 똑같다고생각하고
더해서 +1한걸 나눈값만큼 구매하면 됨
예를 들어 8개필요하면 4개만 사면되는데 8+1//2하면 4>> //이용
7개필요하면 그래도 4개사야하는데 7+1//2 = 4
'''

n = input()
max=0
maxnum = 100
list = [0 for i in range(10)]

for j in n:
    list[int(j)]+=1


list[6]=(list[6]+list[9]+1)//2
list[9]=list[6]

for l in range(10):
    if list [l] > max:
        max = list[l]
        maxnum = l

print(max)