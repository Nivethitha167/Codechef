# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s={0}
    stack=[0]
    while(len(stack)!=0):
        v=stack.pop()
        for i in a:
            if v|i not in s:
                s.add(v|i)
                stack.append(v|i)
        #print(s)
        for i in b:
            if v&i not in s:
                s.add(v&i)
                stack.append(v&i)
        #print(s)
    print(len(s))
