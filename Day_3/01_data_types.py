# Python Data Types

# 1. Numeric Types
# int , float , complex

# 2. Sequence Types
# list , tuple , range

# 3. Text Type
# str

# 4. Mapping Type
# dict

#5. Boolean Type
# bool

print("********************************************************************")

# Numeric Types
a = 10      # int
b = 3.14    # float
c = 2 + 3j  # complex

print("Value of a is : ", a, " and its type is : ", type(a))
print("Value of b is : ", b, " and its type is : ", type(b))
print("Value of c is : ", c, " and its type is : ", type(c))

print("********************************************************************")

# Sequence Types
my_list = [1, 2, 3, 4, 5]          # list
my_tuple = (11, 12, 13, 14, 15)         # tuple
my_range = range(1, 6)              # range

# what is difference between list and tuple
# list is mutable (can be changed) while tuple is immutable (cannot be changed)

#Range is a sequence of numbers, it is used to generate a sequence of numbers

print("Value of my_list is : ", my_list, " and its type is : ", type(my_list))
print("Value of my_tuple is : ", my_tuple, " and its type is : ", type(my_tuple))
print("Value of my_range is : ", my_range, " and its type is : ", type(my_range))

print("********************************************************************")

# Text Type
my_string = "Hello, World!"  # str
print("Value of my_string is : ", my_string, " and its type is : ", type(my_string))

print("********************************************************************")

#Mapping Type

my_dict = {"name": "Alice", "age": 30, "city": "New York"}  # dict
print("Value of my_dict is : ", my_dict, " and its type is : ", type(my_dict))

print("********************************************************************")
 #Boolean Type
is_python_fun = True  # bool
is_sky_blue = False  # bool

print("is_python_fun is : ", is_python_fun, " and its type is : ", type(is_python_fun))
print("is_sky_blue is : ", is_sky_blue, " and its type is : ", type(is_sky_blue))

