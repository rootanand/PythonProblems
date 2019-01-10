# Find out the length of the pallindrome:


def Lengthofpallindrome(N):

    flag=True

    count=0
    X=N
    Reverse=0
    while(N>0):
        temp=(N%10)
        count+=1
        Reverse=Reverse*10+temp
        N=N//10

    if not(Reverse==X):
        return False
        

    print flag
    

    if not(count%2==0):
        return ("The given pallindrome is in odd length")

    return("The given pallindrome is in even length")



#Input
N=input("Enter the Integer: ")
print(Lengthofpallindrome(N))