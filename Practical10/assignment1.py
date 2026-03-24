import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Complete report
print("\n--- Complete Book Report ---")
print(df)

# b) Books by given author
author_name = input("\nEnter author name: ")
print("\nBooks by author:")
print(df[df['author'] == author_name])

# c) Books by given publisher
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by publisher:")
print(df[df['publisher'] == publisher_name])

# d) Cheapest & costliest books
min_price_book = df[df['price'] == df['price'].min()]
max_price_book = df[df['price'] == df['price'].max()]

print("\nCheapest Book:")
print(min_price_book[['title', 'price']])

print("\nCostliest Book:")
print(max_price_book[['title', 'price']])

# e) Sort by year
print("\nBooks sorted by year:")
print(df.sort_values(by='year'))