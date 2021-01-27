/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t!=0)
		{
		    int n,k,s=0,i,x=-1,val;
		    n=sc.nextInt();
		    k=sc.nextInt();
		    int a[]=new int[n];
		    for (i=0;i<n;i++)
		        a[i]=sc.nextInt();
		    Arrays.sort(a);
		    /*for (i=0;i<a.length/2;i++)
		    {
               int temp = a[i];
               a[i]=a[a.length-1-i];
               a[a.length-1-i]=temp;
            }*/
            LinkedHashSet<Integer> l1=new LinkedHashSet<Integer>();
		    l1.add(a[n-1]);
		    s=a[n-1];
		    for(i=n-2;i>-1;i--)
		    {
		        s+=a[i];
		        Iterator iter=l1.iterator();
		        LinkedHashSet<Integer> l2=new LinkedHashSet<Integer>();
		        while(iter.hasNext())
		        {
		            val=(int)(iter.next());
		            l2.add(val);
		            l2.add(a[i]);
		            l2.add(val+a[i]);
		            if (((s-a[i])>=k) && (a[i]>=k))
		            {
		                x=n-i;
		                break;
		            }
		            if (((s-a[i]-val)>=k) && ((val+a[i])>=k))
		            {
		                x=n-i;
		                break;
		            }
		        }
		        if (x!=-1)
		            break;
		        l1=l2;
		    }
		    System.out.println(x);
		    t--;
		}
	}
}
