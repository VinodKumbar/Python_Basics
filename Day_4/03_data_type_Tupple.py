# Tupple is a collection which is ordered and unchangeable (Immutable). Allows duplicate members.
# Tupple is defined by enclosing the items in parentheses ().
# Tupple doesnt support items assignment and menthods like insert(), append() and del.
# Tupple is faster than list because of its immutability.

value = (1, 2.5,"Ohreems", True, 1, 2.5,"Ohreems", True)
print(value)
print(type(value))

value[2] = "Automation-Shop" # This will raise an error because tupple is immutable and does not support item assignment.