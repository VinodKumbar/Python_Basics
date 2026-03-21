file = open('testData.txt')

print(file.read()) # Reads the entire file and returns it as a string

readFile = file.read()
print(readFile)
print("After reading the file, the file pointer is at position: " , file.seek(0)) # Move the file pointer back to the beginning of the file


readChar = file.read(3)
print(readChar) # Reads the next 3 characters from the file and returns them as a string
print("After reading the file, the file pointer is at position: " , file.seek(0))

print("***************** Difference between read and readline ***********************")

# read() method reads the entire file and returns it as a string,
# while readline() method reads the next line from the file and returns it as a string.
# The read() method will read the entire file at once, while readline() will read one line at a time.
# readlines() method reads the entire file and returns it as a list of strings, where each string represents a line in the file.


# read(), readline() and readlines() are all methods used to read data from a file in Python, but they differ in how they read the data and what they return.

readline1 = file.readline()
print(readline1) # Reads the next line from the file and returns it as a string
print("After reading the file, the file pointer is at position: " , file.seek(0))

readline2 = file.readlines()
print(readline2)


file.close()
print("Close the file after reading the data")


# Print line by line using readline() method in a loop
file = open('testData.txt')
while True:
    line = file.readline()
    if not line:  # If the line is empty, we have reached the end of the file
        break
    #print (line)
    print(line.strip())  # Print the line without leading/trailing whitespace
print("After reading the file, the file pointer is at position: " , file.seek(0))
file.close()

#Assignment number 2nd
# Print line by line using readlines() method, get into list and print each line using a for loop
