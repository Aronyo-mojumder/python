     
#*************************************************
#Exception & Error Handiling
#*************************************************    
def divide(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        print("Please enter valid input")
    else:
        print("Result =", division)
    finally:
        print("Program executed")
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b:"))
divide(12, 2)


#*************************************************   
def divide(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        print("Please enter valid input")
    else:
        print("Result =", division)
    finally:

        print("Program executed")
while True:
    try:
        a=int(input("Enter the value of a :"))
        b=int(input("Enter the value of b:"))
    except ValueError :
        print("Please enter valid input")
        break
    continue
        

divide(a, b)