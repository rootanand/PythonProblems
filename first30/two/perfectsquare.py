#Finding the perfect square.

import math
def perfectsquare(N):
    flag=True
    M = math.sqrt(N)
    X = round(M)
    if(M-X)==0:
        return flag
    else:
        return False

N=input("Enter the value of N:")
 print(perfectsquare(N))
