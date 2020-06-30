# cook your dish here
import math
def ispowerof_2(n):
    if math.ceil(math.log10(n)/math.log10(2))==math.floor(math.log10(n)/math.log10(2)):
        return True
    return False
for _ in range(int(input())):
    t=int(input())
    if t==1:
        print(0)
    elif t%2!=0:
        print(int(t/2))
    elif t%2==0:
        if ispowerof_2(t):
            print(0)
        else:
            while(True):
                t=t/2
                if(t%2!=0):
                    print(int(t/2))
                    break
