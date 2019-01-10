# Finding the perfect square and sum of perfect squares between N:
import math

def Isperfectsq(N):
    flag=True
    M=math.sqrt(N)
    X=round(M)

    if not (X-M==0):
        flag=False

    return flag

def Sumofperfectsq(N):
    sum=0
    
    for a in range(1,N+1):

        if(Isperfectsq(a)):
            sum=sum+a

    return sum

N=input("Enter the Value: ")
print(Sumofperfectsq(N))