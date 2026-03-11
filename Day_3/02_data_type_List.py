# List is a collection of items which are ordered and changeable (Mutable). Allows duplicate members.

value = [1, 2.5,"Ohreems", True, 1, 2.5,"Ohreems", True]
print(value)
print(type(value))

print(value[0]) # :: 1

print(value[6]) # :: Ohreems

print(value[1:4]) # from index 1 to index 3 (index 4 is not included) :: 2.5,"Ohreems", True

print(value[-1]) # from end to start :: True

print(value[-2]) # from end to start :: Ohreems

print (value[:4]) # from start to index 3 (index 4 is not included) :: 1, 2.5,"Ohreems", True

print (value)

value.insert(3,"Automation-Shop") # insert value at index 3

print(value)  # [1, 2.5, 'Ohreems', 'Automation-Shop', True, 1, 2.5, 'Ohreems', True]

value[0] = 3.14 # change/update value at index 0

print(value)  # [3.14, 2.5, 'Ohreems', 'Automation-Shop', True, 1, 2.5, 'Ohreems', True]

value.append("Python") # add value at the end of the list
print(value)

del value[5:9] # delete values from index 5 to index 8 (index 9 is not included)
print(value)  # [3.14, 2.5, 'Ohreems', 'Automation-Shop', True]




### Git Notes





