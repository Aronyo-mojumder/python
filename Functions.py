#Find the area of a triangle subject to condition ##
import math
def triangle (a,b,c):
    if (a+b)>c and (b+c)>a and (c+a)>b :
        s=(a+b+c)/2
        Area= math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Area of the Triangle=",Area)
    else :
        print("Triangle is impossible")
    
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :")) 
c=int(input("Enter the value of c :"))     
triangle (a,b,c)

##########################################################################
#Find Prime Numbers Form 1 to n ##

def prime_number (n):
    for i in range(2,n+1,1):
        for j in range(2,n+1,1):
            if i%j == 0 :
                break
        if (i==j):
            print(i)

n=int(input("Enter the value of n :"))
prime_number (n)

#**************************************#

##########################################################################
#Validation of prime number  using function

def prime_number (n):
    
    for i in range(2,n,1):
        if n%i == 0 :
            print("Number is not prime")
            break
    else:
        print("Number is  prime")
x=int(input("Enter the value of n :"))            
prime_number(x)            

       #*****or******
def prime_number ():
    
    n=int(input("Enter the value of n :"))  
    
    for i in range(2,n,1):
        if n%i == 0 :
            print("Number is not prime")
            break
    else:
        print("Number is  prime")
    
prime_number ()




#*********************************************

##########################################################################
#find the  sum of odd number 1 to n

#*while loop
def odd_number (n):
    sum=0
    i=1
    while i <=n :
        if i %2!=0:
            sum=sum+i
        i=i+1
    print(sum)
n=int(input("Enter the value of n :"))          
odd_number (n)

#*forloop **********************************

def odd_number (n):
    sum=0
    i=1
    for i in range (1,n+1,2):
        sum=sum +i  
    print(sum)   
n=int(input("Enter the value of n :"))          
odd_number (n)        

#*********************************************
##########################################################################
#Determination of factorial value

def fact(n):
    fact=1
    for i in range (1,n+1,1):
        fact=fact*i
    print("Factorial number is :",fact)

n=int(input("Enter the value of n :"))    
fact(n)    
##########################################################################
#Determination of Fibonacci series
def fibo(n):
    f1=1
    f2=1
    print(f1)
    print(f2)
    for i in range (3,n+1,1):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
n=int(input("Enter the value of n :"))         
    
fibo(n)    
    
##########################################################################

