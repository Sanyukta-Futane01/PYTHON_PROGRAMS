# Taking integer inputs from the user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(numbers))

# b) Last item in the tuple
print("Last item:", numbers[-1])

# c) Elements in reverse order
print("Tuple in reverse order:", numbers[::-1])

# d) Check if integer 5 is present
if 5 in numbers:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining elements
remaining = numbers[1:-1]
sorted_remaining = tuple(sorted(remaining))

print("After removing first and last items and sorting:", sorted_remaining)