# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    val=n/2
    val=int(val)
    f=n 
    l=n-1
    if (val%2)!=0:
        print(-1)
    else:
        if k<val:
            print(-1)
        else:
            print(val)
            for i in range(1,val+1):
                print(l,f,i)
                if i%2==0:
                    f=f-2
                    l=l-2
                
                
                
    
    
