

def factors(n):
    count=0
    for i in range(1,n+1):
        if (n%i==0):
            count=count+1
    return count
    print count


def IsPrime(n):
    a=factors(n)
    if(a==2):
        print "prime"
    else:
        print "not prime"    

n=input("Enter the number n:")
IsPrime(n)