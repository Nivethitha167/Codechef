# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    s=set(arr)
    if len(arr)-len(s)==0:
        print(len(s)-x)
    elif len(arr)-len(s)<x:
        print(len(arr)-x)
    else:
        print(len(s))
