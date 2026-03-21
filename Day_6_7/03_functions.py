# Functions are reusable piece of code that perform a specific task
# Functions help to break down a large program into smaller and manageable parts, making it easier to read and maintain.
# Functions can take input parameters and return output values, allowing for more flexible and modular code.

def Greeting(name):
    print("Hello, " + name + " Good evening!  Welcome to Python Programming.")

Greeting("Alice")
Greeting("Bob")
Greeting("Charlie")
Greeting("Sudha")
Greeting("Chitra")
Greeting("David")



def AddNumbers(a, b):
    return a+b

result = AddNumbers(50, 100)
print("The Sum of 2 Numbers  is : " + str(result))

result2 = AddNumbers(150, 200)
print("The Sum of 2 Numbers is : " + str(result2))

print("****************************************************************")
# Assignment

# Write a Calculator function that takes two numbers and an operator as input and performs the corresponding arithmetic operation
# (addition, subtraction, multiplication, division) based on the operator provided.
# The function should return the result of the calculation.

#Funtions

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

# Input

num1 = float(input("Enter a number to call Functions: "))
num2 = float(input("Enter another number to call Functions: "))
op = input("Enter Operation ( + , -, *, / ): ")

# Functions Call

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "*":
    print (num1 * num2)
elif op == '/':
    print (num1 / num2)

else:
    print("Invalid Operator. Please enter one of the following: +, -, *, /")


