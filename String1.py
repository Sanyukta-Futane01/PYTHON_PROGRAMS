# Program to count vowels, consonants, spaces and lowercase letters

# Taking input from user
text = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase = 0

for ch in text:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

    if ch == " ":
        spaces += 1

    if ch.islower():
        lowercase += 1

# Printing results
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of spaces:", spaces)
print("Number of lowercase letters:", lowercase)