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

print("************************************************")

obj = [1,2,3,4,5]
for i in obj:
    print("Values of object are : " + str(i))

# Sum of first 10 Natural Numbers
print("*******  Sum of first 10 Natural Numbers  *****************************************")

total = 0
for j in range (1,11):
    total = total + j
   # print(total)
   # print ("Sum of first 10 Natural number is : " , total)
    print("Sum of first 10 Natural number is : " + str(total))


# Print number from 1 to 10 with step of 3

for k in range (1,11,3):
    print(k)
   # print ("Number from 1 to 10 with step of 2")

#Print Number from 0 to 9

for z in range (10):
    print(z)


