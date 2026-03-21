# Read mode is used to read the contents of file
# Write mode is used to write new content to the file.
# If the file already exists, it will overwrite the existing content.
# If the file does not exist, it will create a new file and write the content to it.

# Write mode is denoted by 'w' and read mode is denoted by 'r'

with open("testData.txt","r") as reader:
    print(reader.read())
    reader.seek(0)

    content = reader.readlines()
    print(content)
    reader.seek(0)

    reversed_content = reader.readlines()
    print(reversed_content)


with open("testData.txt","w") as writer:
    writer.write("Flying Fish.\n")
    writer.write("Giant Squid.\n")

with open("testData.txt","a") as appender:
    appender.write("Angel Fish.\n")
    appender.write("Blue Whale.\n")
    appender.write("Cat Fish.\n")
    appender.write("Dolphin.\n")
    appender.write("Eel.\n")
    appender.write("Flying Fish.\n")
    appender.write("Giant Squid.\n")


