# Dictionary is a collection of key-value pairs.
# It is an unordered, mutable, and indexed data type in Python.
# Dictionaries are defined using curly braces {} and the key-value pairs are separated by a colon (:).
# Each key must be unique and immutable (e.g., strings, numbers, tuples), while the values can be of any data type.

values = {"name": "Alice", "age": 30, "city": "New York", 1: "One", 2: "Two"}

#Print Only Names
print(values["name"])  # Output: Alice

#Print 4th value
#print(values[4]) # Output: KeyError: 4

#Print 1st value
print(values[1]) # Output: One

print("********************************************************************")

my_dict = {}
print("Before dynamically adding values to dictionary", my_dict)

my_dict["name"] = "Bob"

my_dict["age"] = 25

my_dict["city"] = "Los Angeles"

print("After dynamically adding values to dictionary", my_dict)

