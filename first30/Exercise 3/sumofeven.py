#Find out the sum of even numbers between given N:

def sumofeven(N):
    sum=0

    for a in range(2,N+1,2):
        if (a%2==0):
            sum+=a
    return sum

N=input("Enter the input: ")
print(sumofeven(N))