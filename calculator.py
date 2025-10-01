import math
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        print("Error! Division by 0 not defined") 
    else:
        return x/y
def square(x):
    return x*x
def sqr_root(x):
    if x<0:
        print("Error! Square root of negative number not defined")
    else:
        return math.sqrt(x)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Square Root")

choice = input("Enter operation to be performed (1/2/3/4/5/6): ")
if choice in ['1','2','3','4']:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

   if choice == '1':
        print("Result:", add(x, y))
   elif choice == '2':
       print("Result:", subtract(x, y))
   elif choice == '3':
        print("Result:", multiply(x, y))
   elif choice == '4':
       print("Result:", divide(x, y))
   elif choice == '5':
       x = float(input("Enter a number: "))
       print("Result:", square(x))
   elif choice == '6':
         x = float(input("Enter a number: "))
         print("Result:", sqr_root(x))
else:
    print("Invalid input")
