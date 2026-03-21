# Inheritance in Python

# One class takes the properties and behaviors of another class.
# The class that inherits is called the child class or subclass and the class being inherited from is called the parent class or superclass.

# Father  -> Parent  / Super Class
# Son     -> Child   / Sub Class

#Son gets
#surname
#habits
#feature

# Parent Class (Base Class) -> gives features
# Child Class (Derived Class) -> takes features




from Constructor import Calculator

class ChildImplementation(Calculator):
    num = 300

    def child_method(self):
        return "This is a method in the Child Class"

    def add(self):                         # Overriding (different set of parameters)
        return self.num + self.a + self.b   # Chil has 3 parameters thus overriding parent add method

obj = ChildImplementation (10, 20)
print(obj.add())   # 300
print(obj.child_method())  # "This is a method in the Child Class"

