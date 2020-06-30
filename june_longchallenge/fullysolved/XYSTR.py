# cook your dish here
for _ in range(int(input())):
    s=input()
    count=0
    flag=0
    for i in range(len(s)-1):
        if(flag):
            flag=0
        else:
            if s[i]=='x':
                if s[i+1]=='y':
                    count+=1
                    flag=1
            elif s[i]=='y':
                if s[i+1]=='x':
                    count+=1 
                    flag=1
    print(count)
