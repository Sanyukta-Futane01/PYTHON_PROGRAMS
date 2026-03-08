# Program to read a file and write content in uppercase to another file

# opening source file
f1 = open("input.txt", "r")   #if file not present, first create a text file called input

# reading content
data = f1.read()

# converting to uppercase
data_upper = data.upper()

# opening destination file
f2 = open("output.txt", "w")

# writing uppercase content
f2.write(data_upper)

# closing files
f1.close()
f2.close()

print("Content copied in uppercase successfully.")