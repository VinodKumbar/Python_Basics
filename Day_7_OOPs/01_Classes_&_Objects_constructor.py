# Classes, Objects and Constructor in Python

# Class is a blueprint for creating Objects. It defines a set of attributes and methods that the objects created from the class will have.

# Object is an instance of a class. It is created using the class and can access the attributes and methods defined in the class.


# Class = Blueprint (Design)

# A class is like a plan or template



#Example

# A Car blueprint defines
# Color
# Model

# Its just a design - not real car

# Construtor in Python is a special method that is automatically called when an object of a class is created.
# It is used to initialize the attributes of the object.
# __init__(self)

#Object = Real Car created from the blueprint

# An Object is the actual item created from the class. It has its own state and behavior.


class car:
    def __init__(self,model, color, speed, luxury):
        self.model = model
        self.color = color
        self.speed = speed
        self.luxury = luxury

# Objects
car1 = car("Benz", "Red", "Ok", "Luxuary" )
car2 = car("Audi", "Blue", "Top Speed", "Ok")

print(car1.model, car1.color, car1.speed, car1.luxury)
print(car2.model, car2.color, car2.speed, car2.luxury)






