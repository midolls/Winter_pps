'''
A027 큰수만들기
어떤 숫자 받으면 k개만큼 지워야함
그리고 가장 크게 만들려면 가장 큰자리숫자가 앞에오게 내림차순으로 정렬해야함
애초에 없앨때도 젤 큰거 두개 놔두면 젤 큰수만들 수 있음
>>> 수를 그대로 둔 채로 가장 크게 만들어야하는 문제였음
'''

def solution(number, k):
    answer = []
    for num in number:
        while answer and k>0 and answer[-1]<num:
            answer.pop()
            k -= 1
        answer.append(num)

    answer = ''.join(answer[:len(number)-k])

    return answer




