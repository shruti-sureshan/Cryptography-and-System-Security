#include <stdio.h>
#include<conio.h>
#include<string.h>
int main(void) {
	// your code goes here


 int i,j,len,rails,count,code[100][100];
    char str[1000];
    clrscr();
    printf("Enter a Secret Message\n");
    gets(str);
    len=strlen(str);
 printf("Enter number of rails\n");
 scanf("%d",&rails);
 for(i=0;i<rails;i++)
 {
  for(j=0;j<len;j++)
  {
   code[i][j]=0;
  }
 }
count=0;
j=0;
while(j<len)
{
if(count%2==0)
{
 for(i=0;i<rails;i++)
 {
  //strcpy(code[i][j],str[j]);
  code[i][j]=(int)str[j];
  j++;
 }

}
else
{

 for(i=rails-2;i>0;i--)
 {
  code[i][j]=(int)str[j];
 j++;
 }
}

count++;
}

for(i=0;i<rails;i++)
{
 for(j=0;j<len;j++)
 {
  if(code[i][j]!=0)
  printf("%c",code[i][j]);
 }

}
printf("\n");
getch();
	return 0;
}
