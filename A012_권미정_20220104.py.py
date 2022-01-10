class Solution:
    def countPrimes(self, n: int) -> int:
        ch=0
        count=0
        if n==0 or n==1 :
            return 0
        else:
            for i in range(2,n):
                for j in range(2,i):
                    if i%j==0:ch+=1
                if ch==0:count+=1
                ch=0
            return count