# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    val=0
    for i in range(0,n-1):
        val+=(abs(a[i]-a[i+1])-1)
        #print(val)
    print(val)
