#sum of digits


def sumofdigits(N):
    sum=0
    while(N!=0):
        x=N%10
        sum=sum+(x)
        N=N/10

    return sum

N=input("Enter the value of N:")
print(sumofdigits(N))