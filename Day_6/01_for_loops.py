# For Loops

# A for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
# IT allows you to execute a block of code repeatedly for each item in the sequence


print("Example 1 : Iterating over a list ")

fruits = ["apple", "banana", "cherry"]
#print(fruits)

print("************************************************")
for fruitName in fruits:
    print(fruitName)

print("************************************************")
print("Example 2 : Iterating over a string ")

for charValue in "Python":
    print(charValue)

print("Example 3 : Iterating over a Tuple ")

tuple_numbers = (1,2,3,4,5)
#print(tuple_numbers)

for number in tuple_numbers:
    print(number)

print("************************************************")

print("Example 4 : Iterating over a dictionary ")

values_dict = {"name": "Alice", "age": 30, "city": "New York", "Country": "USA"}
for key, value in values_dict.items():
    print(key, value)
print(values_dict)

print("************************************************")

for key, value in values_dict.items():
    print(key, value)


print("************************************************")

print("Example 5 : Using range() function in for loop")

for i in range(5,11):    # 11-1 = 10
   # print(i)

    # print(i * 2)  #
    #print ( i * 2)

   print(i,  (i * 5))

   print( str (i) +  " Multiplied by 5 is " + str(i * 5) )