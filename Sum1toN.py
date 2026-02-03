# Sum of All Numbers from 1 to N Program
n=int(input("Enter a positive number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"Sum of all numbers from 1 to {n} is '{sum}'")