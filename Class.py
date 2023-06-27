

##########################################################################
             #CLASS#
##########################################################################

#Find the area of a triangle subject to condition ##

#*********************************************

class Triangle :
    def __init__(self,a,b,c):
        import math

        if (a+b)>c and (b+c)>a and (c+a)>b :
            s=(a+b+c)/2
            Area= math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("Area of the Triangle=",Area)
        else :
            print("Triangle is impossible")
a=int(input("Enter The value of a"))
b=int(input("Enter The value of b"))  
c=int(input("Enter The value of c"))              

Triang=Triangle(a, b, c)



#*********************************************

class QuardenayEQ :
    def __init__(self,a,b,c):
        import math
        d = b**2-(4*a*c)
        if d>0 :
            x1= (-b+ math.sqrt(d))/2*a
            x2= (-b+ math.sqrt(d))/2*a
            print("x1=",x1,"x2=",x2)
        elif d== 0:
            X= -b/2*a
            print("X=",X)
        else :
            print("Root are emaginary")
            
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of a :"))            
c=int(input("Enter the value of a :"))

qrdq=QuardenayEQ(a,b,c)

#*********************************************



