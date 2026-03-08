# Program to copy python file without comments

source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

# opening files
f1 = open(source, "r")
f2 = open(destination, "w")

for line in f1:
    # skipping comment lines
    if not line.strip().startswith("#"):
        f2.write(line)

f1.close()
f2.close()

# printing source file content
print("\nSource File Content:")
f1 = open(source, "r")
print(f1.read())
f1.close()

# printing destination file content
print("\nDestination File Content (Without Comments):")
f2 = open(destination, "r")
print(f2.read())
f2.close()