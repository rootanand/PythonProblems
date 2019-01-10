#print all prime numbers 2 to n:
import math 


def Isprime(n): 
    flag=True
    for i in range(2,int(math.sqrt(n)+1)):
         if n%i==0:
             flag=False
             break
    return flag

def printprimes(M,N):
    count=0
    if(M==1 or M==2):
        print(2)
        count+=1
    if(M%2==0):
        M+=1

        for i in range(M,N+1,2):
            if(Isprime(i)):
                #print(i)
                count+=1
        print(count)


            
M=input("enter the number M:")
N=input("enter the number N:")

if(M>N):
    M,N=N,M
printprimes(M,N)

    