# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=[[0 for i in range(n)] for i in range(n)]
    l=0
    u=0
    r=n-1
    b=n-1
    val=1
    while l<=r and u<=b:
        for i in range(l,r+1):
            a[u][i]=val
            val+=1 
        u+=1 
        for i in range(u,b+1):
            a[i][r]=val
            val+=1 
        r-=1 
        for i in range(r,l-1,-1):
            a[b][i]=val
            val+=1 
        b-=1 
        for i in range(b,u-1,-1):
            a[i][l]=val
            val+=1 
        l+=1
    for i in range(n):
        print(*a[i])
            
