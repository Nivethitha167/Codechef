# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    change_5=0
    change_10=0
    flag=0
    for i in range(n):
        if i==0:
            if a[i]==5:
                change_5+=a[i]
            else:
                flag=1 
                break
        else:
            if a[i]==5:
                change_5+=5
            elif a[i]==10:
                change_5-=5
                change_10+=10
            elif a[i]==15:
                if change_10>0:
                    change_10-=10
                else:
                    change_5-=10
            if change_5<0:
                flag=1 
                #print(change,a[i])
                break
    if(flag):
       print("NO")
    else:
       print("YES")
            
            
            
