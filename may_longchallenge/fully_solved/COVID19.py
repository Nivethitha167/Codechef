# cook your dish here
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    arr=[]
    count=1
    for i in range(0,n-1):
        if (x[i+1]-x[i])<=2:
            count+=1
        else:
            arr.append(count)
            count=1 
    arr.append(count)
    l=len(arr)
    if(l==0):
        print("1 1")
    elif(l==1):
        print(arr[0],end=" ")
        print(arr[0])
    else:
        print(min(arr),end=" ")
        print(max(arr))
            
