#include <stdio.h>
int main(void) {
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        int n,i,j,c=0,b[100]={0},num=0;
        scanf("%d",&n);
        int a[n];
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            b[a[i]]++;
        }
        int max=b[0];
        for(i=1;i<100;i++)
        {
            if(b[i]>max){
              max=b[i];
              num=i;
            }
        }
        for(i=1;i<=n;i++)
        {
            j=i-1;
            if(a[j]!=num)
             c++;
        }
        printf("%d\n",c);
        t--;
    }
	return 0;
}

