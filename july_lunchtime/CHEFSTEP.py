for _ in range(int(input())):
    n,k=(map(int,input().split()))
    arr=list(map(int,input().split()))
    val=""
    for a in arr:
        if a%k==0:
            val=val+"1"
        else:
            val=val+"0"
    print(val)
