# To Find the Kth Even Number

#def Iseven(N):

        #if(N%2==0):
            #return N

def Ktheven(N):
    count=0
    #X=N
    #if(X%2==0):
        #count+=1
    while(count!=K):
        N+=1
        if(N%2==0):
            count+=1
    return N

N=input("Enter the Number: ")
K=input("Enter the Number: ")

print(Ktheven(N))

        