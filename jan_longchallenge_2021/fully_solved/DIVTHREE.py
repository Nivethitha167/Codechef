# cook your dish here
for _ in range(int(input())):
    n,k,d=map(int,input().split())
    arr=list(map(int,input().split()))
    s=sum(arr)
    maxi=0
    if int(s//k)<=d:
        maxi=int(s//k)
    else:
        maxi=d
    print(maxi)
    
