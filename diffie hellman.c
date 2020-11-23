#include<stdio.h>
#include<stdio.h>
#include<math.h>
void main(){
long x,y,n,g,A,B,key1,key2,m,p,s,t;
clrscr();
printf("enter value of g,n,x,y\n");
scanf("%ld%ld%ld%ld",&g,&n,&x,&y);
m=pow(g,x);
A=m%n;
p=pow(g,y);
B=p%n;
s=pow(B,x);
key1=s%n;
t=pow(A,y);
key2=t%n;
printf("A=%ld\n",A);
printf("B=%ld\n",B);
printf("key1=%ld\n",key1);
printf("key2=%ld\n",key2);
if(key1==key2){
printf("connection established"); }
else{
 printf("connection not established");  }
getch();
}
