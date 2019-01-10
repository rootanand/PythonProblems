import math

def Isprime(N):
    flag=True
    if (N<=1):
        flag=False
    if (N==2):
        return flag
        
    for i in range(2,int(math.sqrt(N)+1)):

        if (N%i==0):
            flag=False
            break
    return flag


#N=input("Enter the value of N:")
#print(Isprime(N))  


