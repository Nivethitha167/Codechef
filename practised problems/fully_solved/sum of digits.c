#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    long int n,sum=0;
	    int dig=0;
	    scanf("%ld",&n);
	    while(n!=0)
	    {
	        dig=n%10;
	        sum+=dig;
	        n=n/10;
	    }
	    printf("%ld\n",sum);
	}
	return 0;
}

