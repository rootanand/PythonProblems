# Find the sum of pime numbers less than N:

import math
def Isprime(N): 
    flag=True

    if(N<=1):
        flag=False
    if(N==2):
        return flag

    for i in range(2,int(math.sqrt(N)+1)):
         if N%i==0:
             flag=False
             break
    return flag



def sumofprimes(N):
    sum=2
    for X in range(3,N+1,2):
        if(Isprime(X)):
            sum=sum+X

    return sum

N=input("Enter the value of N:")
print(sumofprimes(N))

    

