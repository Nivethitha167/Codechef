# cook your dish #
    
for _ in range(int(input())):
    n,m=map(int,input().split())
    b=list(map(int,input().split()))
    for i in range(m):
        x,y=map(int,input().split())
    arr = [*enumerate(b)] 
    arr.sort(key = lambda it:it[1]) 
    visited = {k:False for k in range(n)} 
    ans = 0
    for i in range(n): 
        if visited[i] or arr[i][0] == i: 
            continue
        s = 0
        j = i 
        while not visited[j]: 
            visited[j] = True
            j = arr[j][0] 
            s += 1
        if s > 0: 
            ans += (s - 1) 
    print(ans) 
  
