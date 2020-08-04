#include <stdio.h>

int main(void) {
	long int n,i,j,k,l,c=0;
	long long int t;
	scanf("%ld %ld",&n,&t);
	long long int a[n];
	for(i=0;i<n;i++)
	{
	    scanf("%lld",&a[i]);
	}
	for(i=0;i<n-3;i++)
	{
	    for(j=i+1;j<n-2;j++)
	    {
	        for(k=j+1;k<n-1;k++)
	        {
	            for(l=k+1;l<n;l++)
	            {
	               // printf("%lld\n",a[l]);
	                if((a[i]+a[j]+a[k]+a[l])==t)
	                {
	                    //printf("%lld",(a[i]+a[j]+a[k]+a[l]));
	                    c++;
	                }
	            }
	        }
	    }
	}
	printf("%ld\n",c);
	return 0;
}

