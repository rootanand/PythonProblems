# sum of odd numbers between given N:

def sumofodd(N):
    sum=0

    for a in range(1,N+1,2):
        if not (a%2==0):
            sum+=a

    return sum

N=input("Enter the Number: ")
print(sumofodd(N))