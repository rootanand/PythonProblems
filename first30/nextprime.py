import newprime

def nextprime(N):
    
    count=0
    i=N+1
    while(count<1):
        if(newprime.Isprime(i)):
            return i
        i+=1

#N=input("Enter the value:")
#print(nextprime(N))    