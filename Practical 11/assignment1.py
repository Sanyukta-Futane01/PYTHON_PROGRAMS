import matplotlib.pyplot as plt
import numpy as np

# Data
months = [1,2,3,4,5,6,7,8,9,10,11,12]

total_profit = [25000, 27000, 30000, 28000, 32000, 35000, 37000, 36000, 39000, 42000, 45000, 48000]

facecream = [2500, 2600, 2700, 2800, 3000, 3200, 3300, 3400, 3600, 3800, 4000, 4200]
facewash = [1500, 1600, 1700, 1800, 2000, 2100, 2200, 2300, 2400, 2600, 2800, 3000]
toothpaste = [5000, 5200, 5400, 5600, 6000, 6200, 6500, 6700, 7000, 7300, 7600, 8000]

# a) Line Plot - Total Profit
plt.figure()
plt.plot(months, total_profit, marker='o')
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

# b) Multiline Plot - All Products
plt.figure()
plt.plot(months, facecream, label="Face Cream")
plt.plot(months, facewash, label="Face Wash")
plt.plot(months, toothpaste, label="Toothpaste")
plt.title("Product Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()

# c) Bar Chart - Face Cream & Face Wash
x = np.arange(len(months))

plt.figure()
plt.bar(x - 0.2, facecream, width=0.4, label="Face Cream")
plt.bar(x + 0.2, facewash, width=0.4, label="Face Wash")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Face Products Sales")
plt.legend()
plt.show()

# d) Pie Chart - Yearly Sales
total_sales = [
    sum(facecream),
    sum(facewash),
    sum(toothpaste)
]

labels = ["Face Cream", "Face Wash", "Toothpaste"]

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Yearly Sales Distribution")
plt.show()