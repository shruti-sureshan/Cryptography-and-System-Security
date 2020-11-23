Server
import java.io.*;
import java.net.*;
import java.lang.Math;
public class Server{
public static void main(String args[]) throws Exception{
ServerSocket ss=new ServerSocket(6666);
Socket s=ss.accept();
DataInputStream a=new DataInputStream(s.getInputStream());
DataOutputStream b=new DataOutputStream(s.getOutputStream()); 
BufferedReader c=new BufferedReader(new InputStreamReader(System.in));
String str="";
String str2="";
double B;
System.out.println("enter g ");
double g= Double.parseDouble(c.readLine());
b.writeDouble(g);
b.flush();
System.out.println("enter n ");     
double n =  Double.parseDouble(c.readLine());
b.writeDouble(n);
b.flush();
System.out.println("enter x ");     
double x =  Double.parseDouble(c.readLine());
double m=Math.pow(g,x);
double A=(int)m%n;
System.out.println("A is "+(int)A);
b.writeDouble(A);
b.flush();
B=a.readDouble();
System.out.println("B is "+(int)B);
double o=Math.pow(B,x);
double K1=(int)o%n;
System.out.println("key1 is "+(int)K1);
b.writeDouble(K1);
b.flush();
double K2=a.readDouble();
System.out.println("key2 is "+(int)K2);
if(K1==K2){
while(str!="stop"){
System.out.println("waiting for Bobs reply");
str=a.readUTF();
System.out.println("Bob's message is "+str);
System.out.println("enter message");
str2=c.readLine();
b.writeUTF(str2);
b.flush();  } }
else{
System.out.println("keys are not same");  }
b.close();
a.close();
s.close();
ss.close(); }}

Client
import java.io.*;
import java.net.*;
import java.lang.Math;
public class Client{
public static void main(String args[]) throws Exception
{
Socket s=new Socket("localhost",6666);
DataInputStream a=new DataInputStream(s.getInputStream());
DataOutputStream b=new DataOutputStream(s.getOutputStream()); 
BufferedReader c=new BufferedReader(new InputStreamReader(System.in));
String str="";
String str2="";
double A;
double K1;
double B;
double g=a.readDouble();
System.out.println("g is " +(int)g);
double n=a.readDouble();
System.out.println("n is " +(int)n);
System.out.println("enter y ");     
double y =  Double.parseDouble(c.readLine());
double  l=Math.pow(g,y);
 B=(int)l%n;
System.out.println("B is "+(int)B);
b.writeDouble(B);
b.flush();
A=a.readDouble();
System.out.println("A is "+(int)A);
double k=Math.pow(A,y);
double K2=(int)k%n;
System.out.println("key2 is "+(int)K2);
b.writeDouble(K2);
b.flush();
K1=a.readDouble();
System.out.println("key1 is "+(int)K1);
if(K1==K2){
while(!str.equals("stop"))
{
System.out.println("enter message");
str=c.readLine();
b.writeUTF(str);
b.flush();
System.out.println("waiting for Alice's reply");
str2=a.readUTF();
System.out.println("Alice's message is " +str2);  }}
else{
System.out.println("keys are not same");
}
b.close();
a.close();
s.close();        }}
