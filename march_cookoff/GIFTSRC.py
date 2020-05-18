for _ in range(int(input())):
    n=int(input())
    s=input()
    ans1=0
    ans2=0
    if (s[0]=='L' or s[0]=='R'):
        flag=True
    else:
        flag=False
    for i in range(len(s)):
        if(flag):
            if (s[i]=='L'):
                ans1=ans1-1
                flag=False
            if (s[i]=='R'):
                ans1=ans1+1
                flag=False
        else:
            if (s[i]=='U'):
                ans2=ans2+1
                flag=True
            if (s[i]=='D'):
                ans2=ans2-1
                flag=True
    print(ans1,end=" ")
    print(ans2)
