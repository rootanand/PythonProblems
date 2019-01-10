# Find the given number is pallindrome or not:

def Ispallindrome(N):

    flag=True

    X=N
    Reverse=0
    while(N>0):
        temp=(N%10)
        Reverse=Reverse*10+temp
        N=N//10

    if not(Reverse==X):
        flag=False

    return flag

#Input
#N=input("Enter the Integer: ")
#print(Ispallindrome(N))