import newprime

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
#print(previous(N))   
