# Strings are sequence of characters.
# They are used to store and manipulate text.
# In Python, strings are enclosed in either single quotes (' ') or double quotes (" ").
# You can also use triple quotes (''' ''' or """ """) for multi-line strings.

#String Examples

str = 'Hello, World!'  # Using single quotes
print(str)

str1 = "Welcome to Python Programming"  # Using double quotes
print(str1)

str3 = '''
This is a multi-line string.
It can span multiple lines.
string went up to 3rd line '''  # Using triple quotes
print(str3)

print("********************************************************************")

str4 = "Python Programming is fun!"
print(str4[5])  # Accessing the 6th character (index starts at 0)

print(str4[0:6])  # Slicing the string from index 0 to index 5 (index 6 is not included)

print("********************************************************************")

# Concatenation of strings
print(str + " " + str1)  # Concatenating str and str1 with a space in between


print("********************************************************************")

# if str1 contains the word "Python"
if "Python" in str1:
    print("Yes, 'Python' is present in str1")
else:
    print("No, 'Python' is not present in str1")

# if str4 exists in str1
if str4 in str1:
    print("Yes, str4 is present in str1")
else:
    print("No, str4 is not present in str1")