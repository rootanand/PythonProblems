def Isprime(n): 
    flag=True
    for i in range(2,n**1/2):
         if n%i==0:
             flag=False
             break
    print flag
n=input("enter the number n:")
print(Isprime(n)) 
print n 
    