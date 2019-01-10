# First digit of the given integer:


def Firstdigit(N):

    flag=True    

    count=0
    A=N
    while(N>10):
        N%10
        count+=1
        N=N//10

    X=(A//(10**count))
    Y=(A%10)

    print("The First digit of the given integer", X)
    print("The Last digit of the given integer",Y)

    if (X!=Y):
        flag=False

    return flag

N=input("Enter the value: ")
print(Firstdigit(N))




    







