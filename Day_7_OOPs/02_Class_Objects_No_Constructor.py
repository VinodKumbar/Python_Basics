class calculator:




    def add(self, a,b):
        return a+b

    # default constructor is used when we do not define any constructor in the class.
    # IT is automatically provided by Python and does not take any parameters.
    # It initializes the object with default values.
    # def__init__(self):
    # print ("I am called automatically when object is created")

    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b != 0:
            return a/b
        else:
            return "Error: Division by zero is not allowed."
    def name(self):
        print("Name of Class i,.e I am Calculator")

# Create an Object of the calculator class and syntax to create an object of a class

obj = calculator()     # syntax to create an object of a class is : object_name = ClassName()
obj.add(1,2)
obj.subtract(3,4)
obj.multiply(5,6)
obj.divide(12,2)
obj.divide(5,0)
obj.name()

# In the above code, we have defined a Class called Calculator with four methods: add, subtract, multiply, and divide.
# We have created an object of the Calculator class and called each method with different arguments to perform the corresponding arithmetic operations.
# The divide method also includes error handling for division by zero.

# Print in the console 1st assignment

print("Addition of 1 and 2 is : " + str(obj.add(1,2)))
print("Subtraction of 3 and 4 is : " + str(obj.subtract(3,4)))
print("Multiplication of 5 and 6 is : " + str(obj.multiply(5,6)))
print("Division of 12 and 2 is : " + str(obj.divide(12,2)))
print("Division of 5 and 0 is : " + str(obj.divide(5,0)))
print("Name of the Class is : " + str(obj.name()))


