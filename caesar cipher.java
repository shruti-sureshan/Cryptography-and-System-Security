 import java.util.Scanner;
   public class App{
   public static void main(String[] args) {
   Scanner sc=new Scanner(System.in);
    String result="";
    String dresult="";
    String str="";
    String d="";
    int i,x,m,j;
    System.out.println("Enter plain text:");
    String p=sc.nextLine();
    p=p.replace(" ","");
    System.out.println("Enter key:");
    int k=sc.nextInt();
    int n=p.length();
         System.out.println("Caesar Cipher is:");
    for (i=0;i<n;i++)
    {
        char ch=(char)(((int)p.charAt(i)+k-65)%26+65);
        result=result.concat(Character.toString(ch));
    }
        System.out.println("Encrypted text="+result);
    
         for (i=0;i<n;i++)
    {
        char ch=(char)(((int)result.charAt(i)-k-65)%26+65);
        dresult=dresult.concat(Character.toString(ch));
    }
        System.out.println("Decrypted text="+dresult);
    
        
   }
     }
