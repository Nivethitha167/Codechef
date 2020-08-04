#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	 long int a,b,i;
	 int c=0;
	 scanf("%d %d",&a,&b);
	 for(i=a;i<=b;i++)
	 {
	     if(i%10==2 || i%10==3 || i%10==9)
	      c++;
	 }
	 printf("%d\n",c);
	}
	return 0;
}

