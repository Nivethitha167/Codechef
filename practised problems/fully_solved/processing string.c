#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t!=0)
	{
	    char str[1000];
	    int sum=0;
	    scanf("%s",str);
	    int len=strlen(str);
	    for(int i=0;i<len;i++)
	    {
	        if(isdigit(str[i]))//if((str[i]-48)>=0 && (str[i]-48<=9))
	        {
	            sum+=str[i]-48;
	        }
	    }
	    printf("%d\n",sum);
	    t--;
	}
	return 0;
}

