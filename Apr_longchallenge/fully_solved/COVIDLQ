for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    pos=0
    flag=True
    for i in range(n):
        if a[i]==1 and count==0:
            count+=1 
            pos=i
            flag=True
        elif a[i]==1 and count==1:
            count=1
            if(i-pos < 6):
                flag=False
                break
            pos=i
    if(flag):
        print("YES")
    else:
        print("NO")
            
