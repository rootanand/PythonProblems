#Count the Number of integers in a Given Number

def countdigits(N):

    count=0

    while(N>0):
        N%10
        count+=1
        N=N//10

    return count

#N=input("Enter the Number:")
#print(countdigits(N))
