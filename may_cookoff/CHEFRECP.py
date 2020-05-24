# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    visited=[0]*1001
    for i in range(len(a)-1):
        if a[i]!=a[i+1]:
            visited[a[i]]+=1 
    visited[a[n-1]]+=1 
    flag=True
    for i in visited:
        if i>1:
            flag=False
    count={}
    l=[]
    val=True
    if(flag):
        for i in a:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for key in count:
            if count[key] in l:
                val=False
                break
            l.append(count[key])
        #print(*l)
        if(val):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
            
            
