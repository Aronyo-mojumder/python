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
