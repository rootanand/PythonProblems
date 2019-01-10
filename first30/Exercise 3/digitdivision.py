# Check if all digits of a given N Divides N:


def Digitdivision(N):
    
    flag=True

    I=N
    while (N>0):
        x=N%10
        N=N//10
        if not (I%x==0):
            flag=False
            break

    return flag

#Enter the Input:

#N=input("Enter the Input:")
#print(Digitdivision(N))