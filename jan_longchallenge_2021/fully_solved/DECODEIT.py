# cook your dish here
for _ in range(int(input())):
    alp="abcdefghijklmnop"
    n=int(input())
    s=input()
    slab=0
    length=len(s)
    f=0
    l=4
    while(True):
        if slab>=length:
            break
        s1=s[f:l]
        f=l
        l+=4
        s1=int(s1,2)
        print(alp[s1],end="")
        slab+=4
    print()
