
##########################################################################
                   #Inheritance#
##########################################################################
       #single Inheritance
#*********************************************
class add:
    def sum(self):
   
        self.a = int(input("Enter the value of a: "))
        self.b = int(input("Enter the value of b: "))    
        
        self.sum = self.a + self.b
        print("Sum:", self.sum)

class subtract(add):
    def subtraction(self):
        self.sub = self.a - self.b
        print("Sub:", self.sub)

obj=subtract()
obj.sum()
obj.subtraction()

 
        
       #### OR ####

class Human :
    def __init__(self,name):
       
        self.name=name
    def show_name1 (self):
        print(self.name) 
        print ("Human class ") 
        
class robot (Human) :
    def __init__(self,name):
        self.name=name    
    def show_name2 (self):
        
        print(self.name)    
        print ("Robot class ")    
 
obj=robot("Aronyo") 
obj.show_name1()
obj.show_name2()     

#*********************************************
        #Multilevel Inheritance
#*********************************************
class add:
    def sum(self):
   
        self.a = int(input("Enter the value of a: "))
        self.b = int(input("Enter the value of b: "))    
        
    
        self.sum = self.a + self.b
        print("Sum:", self.sum)

class subtract(add):
    def subtraction(self):
        self.sub = self.a - self.b
        print("Sub:", self.sub)

class multiple(subtract):
    def multiplication(self):
        self.mul = self.a * self.b
        print("Mul:", self.mul)

obj=multiple() 
obj.sum()
obj.subtraction()  
obj.multiplication()     

           #### OR ####
           

class Human :
    def __init__(self,name):
       
        self.name=name
    def show_name1 (self):
        print(self.name) 
        print ("Human class ") 
        
class robot (Human) :
    def __init__(self,name):
        self.name=name    
    def show_name2 (self):
        
        print(self.name)    
        print ("Robot class ")   

class cartoon (robot):
    def __init__(self,name):
        self.name=name    
    def show_name3 (self):
        
        print(self.name)    
        print ("Cartoon class ") 


Obj=cartoon("Doraemon") 
Obj.show_name1()
Obj.show_name2()
Obj.show_name3()
       
    

#*********************************************
        #Hierarchical Inheritance
#*********************************************
           
class Add:
    def sum(self):
   
        self.a = int(input("Enter the value of a: "))
        self.b = int(input("Enter the value of b: "))    
        
    
        self.sum = self.a + self.b
        print("Sum:", self.sum)

class subtract(Add):
    def subtraction(self):
        self.sub = self.a - self.b
        print("Sub:", self.sub)

class multiple(Add):
    def multiplication(self):
        self.mul = self.a * self.b
        print("Mul:", self.mul)           


obj = multiple()  
obj.sum() 
obj.multiplication()  

obj = subtract()
obj.sum()
obj.subtraction()  


   #### OR ####
           

class Human :
    def __init__(self,name):
       
        self.name=name
    def show_name (self):
        print(self.name) 
        print ("Human class ") 
        
class robot (Human) :
    def __init__(self,name):
        self.name=name    
    def show_name (self):
        
        print(self.name)    
        print ("Robot class ")   

class cartoon (Human):
    def __init__(self,name):
        self.name=name    
    def show_name (self):
        
        print(self.name)    
        print ("Cartoon class ") 


Obj = cartoon("Doraemon") 
Obj.show_name()

Obj = robot("Doraemon") 
Obj.show_name()       



#*********************************************
        #Multiple Inheritance
#*********************************************

           
class Add:
    def sum(self):
   
        self.a = int(input("Enter the value of a: "))
        self.b = int(input("Enter the value of b: "))    
        
    
        self.sum = self.a + self.b
        print("Sum:", self.sum)

class subtract:
    def subtraction(self):
        self.sub = self.a - self.b
        print("Sub:", self.sub)

class multiple(Add,subtract):
    def multiplication(self):
        self.mul = self.a * self.b
        print("Mul:", self.mul)     
Obj= multiple()
Obj.sum() 
Obj.subtraction()
Obj.multiplication()      
        

   #### OR ####
           

class Human :
    def __init__(self,name):
        
        self.name=name
    def show_name1(self):
        print(self.name) 
        print ("Human class ") 
        
class robot  :
    def __init__(self,name):
        self.name=name    
    def show_name2 (self):
        
        print(self.name)    
        print ("Robot class ")   

class cartoon (Human,robot):
    def __init__(self,name):
        self.name=name    
    def show_name3 (self):
        
        print(self.name)    
        print ("Cartoon class ") 


Obj = cartoon("miju") 
Obj.show_name1()

Obj.show_name3()       

##########################################################################
                  #Polymorphism#
##########################################################################

class math1():
    def __init__(self,a,b):
        self.a=a
        self.b=b
       
    def Multiple(self):
        result= self.a*self.b
        print("Mul=",result)
        
class math2 ():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def Multiple(self):
        
        result = self.a*self.b*self.c
        print("Mul=",result)   

obj1=math1(6,8)
obj2=math2(9,7, 9)

obj1.Multiple()
obj2.Multiple()


#*********************************************
        #Method Overriding
#*********************************************
class parent ():
    def __init__(self):
        self.value = "Computer "
    def show(self):                      #show over read
        print(self.value)

class Child(parent ):
    def __init__(self):
        self.value = " Laptop"
    def show(self):
        print(self.value)

obj1=parent()
obj2=Child()

obj1.show()
obj2.show()


#*********************************************
        #Method Overloding
#*********************************************
class Area :
    def find_Area (self,x=None,y=None):
        if x!=None and y!=None :
            Area= x*y
            print("Area = ",Area)
        elif y!=None :                    #Area Overload
            Area= x*x
        else :
            print("Nothing")
obj=Area()
obj.find_Area(4,9)
obj.find_Area(4)
obj.find_Area(5,8)



##########################################################################
                  #Abstraction#
##########################################################################
from abc import ABC,abstractmethod
class Car (ABC):
    @abstractmethod
    def mileage(self):
        pass
    def color(self):
        print("Black")
class TATA(Car):
    def mileage(self):
        print("Mileage is 40 kmph")

class BMW (Car):
    def mileage(self):
        print("Mileage is 45 kmph")
    

class TOYOTA(Car):
    def mileage(self):
        print("Mileage is 50 kmph")


obj1=TATA()
obj2=BMW()
obj3=TOYOTA()

obj1.mileage()
obj1.color()
obj2.mileage()
obj3.mileage()


##########################################################################
                  #Encapsulation#
##########################################################################

class Person:
    def __init__(self, name, age):
        self.name = name              # Public attribute
        self._age = age               # Protected attribute
        self.__address = "Jashore"    # Private attribute

    def display_info(self):
        print("Name:", self.name)     # Public method
        print("Age:", self._age)      # Protected method
        self.__private_method()       # Private method

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

person= Person("Alice", 30)

print(person.name)          
print(person._age)

person.display_info()
person._person._protected_method()
person._person__private_method()

