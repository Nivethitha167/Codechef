# cook your dish here
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    sort=sorted(arr)
    c=0
    for j in range(n):
        if sort[c]==arr[j]:
            c+=1;
    print(n-c)
