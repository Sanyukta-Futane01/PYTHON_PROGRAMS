# Program to store user entered integers in a tuple

# Taking input from the user
numbers = input("Enter a series of integers separated by space: ")

# Converting input string to integer tuple
numbers_tuple = tuple(map(int, numbers.split()))

# Display the tuple
print("The tuple of integers is:", numbers_tuple)