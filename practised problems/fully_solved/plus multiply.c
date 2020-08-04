#include <stdio.h>

int main(void) {
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        int count1=0,count2=0,pair1=0,pair2=0,b=0;
        long int n;
        scanf("%ld",&n);
        long long int a[n];
        for(int i=0;i<n;i++)
        {
            scanf("%lld",&a[i]);
            if(a[i]==0)
             count1++;
            if(a[i]==2)
             count2++;
        }
        /*if(count1>=2)
        {
          while(count1!=0)
          {
            count1--;
            pair1+=count1;
           }
        }
        if(count2>=2)
        {
            while(count2!=0)
            {
                count2--;
                pair2+=count2;
            }
        }*/
        pair1=(count1*(count1-1))/2;
        pair2=(count2*(count2-1))/2;
        b=pair1+pair2;
        printf("%d\n",b);
        t--;
    }
	return 0;
}

