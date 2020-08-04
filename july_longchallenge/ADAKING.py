for _ in range(int(input())):
    n=int(input())
    a=[["X" for i in range(8)] for i in range(8)]
    a[0][0]="O"
    val=1 
    flag=0
    for i in range(8):
        for j in range(8):
            if val==n:
                flag=1 
                break
            elif i==0 and j==0:
                pass
            else:
                a[i][j]="."
                val+=1 
        if(flag):
            break 
    for i in range(8):
        s=""
        print(s.join(a[i]))
