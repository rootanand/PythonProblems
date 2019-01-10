# Last digit of the given integer

import firstdigit

def Lastdigit(N):

    X=N%10
    return X

    if(Firstdigit(N)==Lastdigit(N)):
        print("First and last digit are same")

N=input("Enter the value of N: ")
Lastdigit(N)

