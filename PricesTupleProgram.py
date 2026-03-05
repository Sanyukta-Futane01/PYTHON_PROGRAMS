# Taking prices input from user
prices = tuple(map(float, input("Enter prices of sold items separated by space: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Price of cheapest item
print("Cheapest item price:", min(prices))

# c) Price of costliest item
print("Costliest item price:", max(prices))

# d) Price list in ascending order
ascending = tuple(sorted(prices))
print("Prices in ascending order:", ascending)

# e) Number of costliest items sold
costliest = max(prices)
count_costliest = prices.count(costliest)

print("Number of costliest items sold:", count_costliest)