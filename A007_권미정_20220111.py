'''A007'''

data = list(map(int,input().split()))

if data ==  sorted(data):
    print("ascending")
elif data == list(reversed(sorted(data))):
    print("descending")
else :
    print("mixed")

