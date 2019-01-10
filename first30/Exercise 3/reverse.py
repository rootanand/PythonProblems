#Reverse a Given Number

def Reverseint(N):
    Reverse=0
    while(N>0):
        temp=(N%10)
        Reverse=Reverse*10+temp
        N=N//10
    return Reverse

#Input
#N=input("Enter the Integer:")
#print(Reverseint(N))