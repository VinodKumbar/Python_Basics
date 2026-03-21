# what is construtor
# Construtor is a special method in Python that is automatically called when an object of a class is created.
# It is used to initialize the attributes of the object.
# The Constructor method is defined using the "__init__" keyword
# Self keyword is a refernce to the current instance of the class
# It is used to access the attributes and methods of the class in Python
# The Self paraments is always the first parameter of the constructor method and is automatically passed by Python when an object is created from the class.
# Construtor names should always be '__init__' and it should always take at least one parameter which is 'self' and it can take additional parameters as needed to initialize the attributes of the object.


class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"


if __name__ == "__main__":                  # This line is used to control when your code should run
                                            # Run this code only if this file is executed directly (not when you import)
    calculator = Calculator(30,5)      # Create an object of the Calculator class and pass the values 5 and 6 to the constructor

    print("Addition of 30 and 5 is : " + str(calculator.add()))
    print("Subtraction of 30 and 5 is : " + str(calculator.sub()))
    print("Multiplication of 30 and 5 is : " + str(calculator.multiply()))
    print("Division of 30 and 5 is : " + str(calculator.divide()))
