#include <stdio.h>
#include <math.h>
long long int n;
long long int a[9],b[9],ra,rb;
void king_moves(int ra,int rb)
{
    long long int x[9]={0,-1,-1,0,-1,1,0,1,1};
    long long int y[9]={0,-1,0,1,1,1,-1,0,-1};
    for(int i=0;i<9;i++)
    {
        a[i]=x[i]+ra;
        b[i]=y[i]+rb;
    }
}
int main(void) {
	int t,flag,i,c,d;
	scanf("%d",&t);
	if(t<=5){
	for(d=1;d<=t;d++)
	{
	   c=0;
	   scanf("%lld",&n);
	   long long int k[n],l[n];
	   for(i=0;i<n;i++)
	   {
	       scanf("%lld %lld",&k[i],&l[i]);
	   }
	   scanf("%lld %lld",&ra,&rb);
	   king_moves(ra,rb);
	   for(i=0;i<9;i++)
	   {
	       flag=1;
	       for(long long int j=0;j<n;j++)
	       {
	         if((abs(a[i]-k[j])==2 && abs(b[i]-l[j])==1) || (abs(a[i]-k[j])==1 && abs(b[i]-l[j])==2))
	             flag=0;
	         
	       }
	       if(flag==0)
	         c++;
	   }
	   if(c==9)
	     printf("YES\n");
	   else
	     printf("NO\n");
	}
	}
	   return 0;
}


