# cook your dish here
for _ in range(int(input())):
    x,y,l,r=(map(int,input().split()))
    val=x|y
    if x==0 or y==0:
        print(0)
    elif l==0 and r>=val:
        print(val)
