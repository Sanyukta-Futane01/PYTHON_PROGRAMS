arr = []

print("Enter 10 integers:")
for i in range(10):
    arr.append(int(input()))

# Reverse array
reverse_arr = arr[::-1]

print("Original Array:", arr)
print("Reversed Array:", reverse_arr)