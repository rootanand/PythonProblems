def Isprime(n): 
    flag=True
    for i in range(2,n**1/2):
         if n%i==0:
             flag=False
             break
    return flag


x=input("enter:")
if(Isprime(x)):
    print x


    
    