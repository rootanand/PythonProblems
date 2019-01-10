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


def previousprime(N):
    if(N<2):
        return "no primes"
    count=0
    i=N-1
    while(count<1):
        if(newprime.Isprime(i)):
            return i
        i-=1

#N=input("Enter the value:")
#print(nextprime(N))   




def immediateprime(n):

    x1=nextprime(n)
    y1=x1-n

    x2=previousprime(n)
    y2=n-x2

    if(y1<=y2):
        return x1

    else:
        return x2

n=input("Enter the value of ")
print(immediateprime(n))