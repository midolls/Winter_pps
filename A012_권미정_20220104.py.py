class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1 or n==2 :
            return 0
        prime = [1] *(n)
        prime[0]=0
        prime[1]=0


        for i in range(2,n):
            if prime[i]:
                prime[i+i:n:i] = [0]*len(prime[i+i:n:i])
        return sum(prime)

