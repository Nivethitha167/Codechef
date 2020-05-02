for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a.reverse()
    val=0
    for i in range(n):
        if(a[i]-i <=0):
            val+=0
            break
        val+=(a[i]-i)
    print(val%1000000007)    
