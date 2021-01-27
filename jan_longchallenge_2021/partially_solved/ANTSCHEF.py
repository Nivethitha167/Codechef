# cook your dish here
for _ in range(int(input())):
    n=int(input())
    pos=0
    neg=0
    for i in range(n):
        arr=list(map(int,input().split()))
        m=arr[0]
        arr=arr[1:]
        for i in arr:
            if i>0:
                pos+=1 
            else:
                neg+=1
    print(pos*neg)    
