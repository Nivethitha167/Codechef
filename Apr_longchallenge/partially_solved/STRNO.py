import math
def prime(x):
    flag=True
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            flag=False
            break
    if(flag):
        return True
    else:
        return False
        
for _ in range(int(input())):
    x,k=map(int,input().split())
    flag=False
    if(k==1 and x>=2):
        flag=True
    elif(x>=(k*2)):
        if(not(prime(x))):
            flag=True
    if(flag):
        print(1)
    else:
        print(0)
