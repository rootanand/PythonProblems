# Finding perfect squares by addding n odd numbers.

def perfectsq(N):
    flag=False
    sum=0
    for i in range(1,N,2):
        sum=sum+i
        if (sum==N):
            return True
        

    return flag


N=input("Enter the value of N:")
print(perfectsq(N))        
