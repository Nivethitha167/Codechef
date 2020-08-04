#include <stdio.h>
#define max 1000001

int main(void) {
	long int n,i,a[max]={0},val,m=0;
	scanf("%ld",&n);
	for(i=0;i<n;i++)
	{
	    scanf("%ld",&val);
	    m=(val>m)?val:m;
	    a[val]++;
	}
	//rintf("%ld",m);
	for(i=0;i<=m;i++)
	{
	    if(a[i])
	    {
	        while(a[i]!=0)
	        {
	            printf("%ld\n",i);
	            a[i]--;
	        }
	    }
	}
	return 0;
}

