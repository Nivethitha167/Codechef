# cook your dish here
for _ in range(int(input())):
    n=int(input())
    chef=0
    morty=0
    for i in range(n):
        a,b=map(str,input().split())
        al=[]
        bl=[]
        for i in a:
            al.append(int(i))
        for i in b:
            bl.append(int(i))
        if(sum(al)>sum(bl)):
            chef+=1 
        elif(sum(al)<sum(bl)):
            morty+=1 
        else:
            chef+=1 
            morty+=1 
    if(chef>morty):
        print(0,chef)
    elif(chef<morty):
        print(1,morty)
    else:
        print(2,chef)
            
            
            
            
