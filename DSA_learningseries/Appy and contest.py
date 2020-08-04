# cook your dish here
import math
for _ in range(int(input())):
    n,a,b,k=map(int,input().split())
    lcm=(a*b)/math.gcd(a,b)
    #print(type(lcm))
    val=math.floor(n/a)+math.floor(n/b)-(2*(math.floor(n/lcm)))
    #print(type(val))
    if val>=k:
        print("Win")
    else:
        print("Lose")
    
