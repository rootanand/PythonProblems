#print count of prime numbers 2 to n:
import math
def Isprime(n): 
    flag=True
    for i in range(2,int(math.sqrt(n)+1)):
         if n%i==0:
             flag=False
             break
    return flag

def countprimes(N):
    count=0
    if (N>=2):
        count+=1



    for i in range(3,N+1,2):
        if(Isprime(i)):
            count+=1
    print("There are {0} prime numbers from 2 to{1}".format(count,N))
            
N=input("enter the number N:")
countprimes(N)

    