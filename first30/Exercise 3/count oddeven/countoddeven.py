#Count the even and odd digits in an integer:

def countoddeven(N):

    oddcount=0
    evencount=0

    while(N>0):
        x=N%10
        N=N//10
        
        if(x==1 or x%2!=0):
            oddcount+=1
        elif(x!=0 and x%2==0):
            evencount+=1

    print ("Total odd numbers in the given integer", oddcount)
    print ("Total even numbers in the given integer", evencount)

#N=input("Enter the integer:")
#countoddeven(N)
