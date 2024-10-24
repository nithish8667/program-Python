import java.util.Scanner;  
public class AdamNumberExample  
{  
static int reverseDigits(int num)  
{       
int rev = 0;    
while (num > 0)  
{    
rev = rev * 10 + num % 10;  
num = num / 10;
}   
return rev;  
}   
static int square(int num)  
{    
return (num * num);  
}    
static boolean isAdamNumber(int num)  
{  
int a = square(num);  
int b = square(reverseDigits(num));  
if (a == reverseDigits(b))  
return true;  
return false;         
}   
public static void main(String args[])  
{  
Scanner sc = new Scanner(System.in);  
System.out.print("Enter the number: ");   
int num = sc.nextInt();  
if (isAdamNumber(num))  
System.out.println(num+ " is an Adam number.");  
else  
System.out.println(num+ " not an Adam number.");      
}  
}  