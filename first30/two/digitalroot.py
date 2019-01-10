#Digital root


def digitalroot(N):
    root=0
    while(N>0 or root>9):
        if(N==0):
            N=root
            root=0

        root+=N%10
        N=N/10

    return root

N=input("Enter the value of N:")
print(digitalroot(N))