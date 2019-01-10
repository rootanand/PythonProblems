#print n prime numbers:

def Isprime(n): 
    flag=True
    for i in range(2,n**1/2):
         if n%i==0:
             flag=False
             break
    return flag

def nprimes(N):
    count=0
    if (N>=2):
        #print(2)
        count+=1



    i=3
    while(count!=N):
        if(Isprime(i)):
            count+=1
        i=i+2
    print i
    
    
            
N=input("enter the number N:")
nprimes(N)