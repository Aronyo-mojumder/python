
##########################################################################
                  #Inter#
##########################################################################

a=[4,8,9,6,8]
vlalu_iter = iter(a)
print(next(vlalu_iter))
print(next(vlalu_iter))
print(next(vlalu_iter))
print(next(vlalu_iter))
print(next(vlalu_iter))



 #*************************************************
class Tast :
     def __init__(self,limit):
         self.limit = limit
     def __iter__(self):
         self.a=10
         return self
     def __next__(self):
         a=self.a
         if a >self.limit:
             raise StopIteration
         self.a =self.a+1
         return a
for i in Tast(10):
     print(i) 
for i in Tast(67):
     print(i)     
     
     
 #*************************************************
     
class test :
    def __init__(self,limit):
        self.limit = limit
        self.a=20
    def __iter__(self):
       
        return self
    def __next__(self):
        if self.a < self.limit :
            
            
            raise StopIteration
        c_value = self.a
        self.a= self.a -1
        return c_value
for i in test (-7) :
    print(i)
       
       
    
 

##########################################################################
                  #Generator#
##########################################################################  
 

def number_genarator(n):
    for i in range(n):
        yield i
genarator =number_genarator(7)    
print(next(genarator)) 
print(next(genarator)) 
print(next(genarator)) 
print(next(genarator))     
print(next(genarator)) 
print(next(genarator)) 
print(next(genarator))   
print(next(genarator)) 
print(next(genarator)) 
    
#*************************************************
#Generator for fibonacci Numbers
#*************************************************    
 
def fib(n):
    f1 = 1
    f2 = 1
    yield f1
    yield f2
    for i in range(n-3):
        f3 = f1 + f2
        yield f3
        f1 = f2
        f2 = f3

fibo = fib(10)
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))    
print(next(fibo))
print(next(fibo))
print(next(fibo))  


#Generator for fibonacci Numbers
#***********************************************   

def series(n):
    for i in range (1,n+1,2):
        yield(i)
series=series(8)        
print(next(series))
print(next(series))
print(next(series))


##########################################################################
                  #Dacorator#
##########################################################################  

def student(info):
    def Student_name ():
        print("Aronyo Mojumder")
        info()
    return Student_name
    
    
@student
def Department():
    print("Computer")

Department()    




 #*************************************************


def student(func):
    
    def detels():
        def name():
            print("Aronyo Mojumder")
            func()
        name()
        def semester():
            print("3rd")
            func()
        semester()  
    return detels

@student

def Department():
    print("Computer")

Department()



































