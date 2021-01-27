# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    b.reverse()
    s1=sum(a)
    s2=sum(b)
    mini=min(n,m)
    flag=1
    swap=0
    if s1>s2:
        print(swap)
    else:
        for i in range(0,mini):
            val=a[i]
            a[i]=b[i]
            b[i]=val
            swap+=1
            if sum(a)>sum(b):
                print(swap)
                flag=0
                break
        if(flag):
            print(-1)
        
        
