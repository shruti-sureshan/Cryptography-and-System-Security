import static java.lang.Math.abs;
import static java.lang.Math.pow;
import java.util.Scanner;
public class App {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
       System.out.println("Enter plain text : ");
       String pt=sc.next();
       char[] arr=pt.toCharArray();
       int x=arr.length;
        double d,p=7,q=17,e=5,k=1;
        double n=p*q;
        double n1=(p-1)*(q-1);
        d=k*n1+1;
        while(d%e!=0){
            k++;
            d=((k*n1)+1);
        }
        d=d/e;
        System.out.println("d="+d);
        double[] c=new double[x];
      String t="";
        System.out.println("Cipher text");
        for(int i=0;i<arr.length;i++){     
        c[i]=(pow(arr[i]-97,e))%n;
        //System.out.println(c[i]);
                t=t+(char)((abs((int)c[i]-97)%26)+97);
            System.out.println(((abs((int)c[i]-97)%26)));   
        }
       System.out.println("Encryption=" +t);     
String dec="";
for(int j=0;j<arr.length;j++){
double ans=1;
    for(int i=1;i<=d;i++){
    ans=(ans*c[j])%n;   
    }
dec=dec+(char)(ans+97);
        }
        System.out.println("Decryption= "+dec);} 
    }
