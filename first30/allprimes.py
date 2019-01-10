#print all prime numbers 2 to n:

def Isprime(n): 
    flag=True
    for i in range(2,n**1/2):
         if n%i==0:
             flag=False
             break
    return flag

def printprimes(N):
    if (N>=2):
        print(2)

        for i in range(3,N+1,2):
            if(Isprime(i)):
                print(i)
            
N=input("Enter the number N:")
print ("primes")
printprimes(N)

    