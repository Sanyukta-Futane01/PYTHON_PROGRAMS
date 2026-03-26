import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

print("\n--- Employee Data ---")
print(df)

# a) Employees in Automotive domain
print("\nEmployees in Automotive domain:")
print(df[df['Department'] == "Automotive"])

# b) Search employee by ID
emp_id = int(input("\nEnter Employee ID to search: "))
result = df[df['Employee ID'] == emp_id]

if not result.empty:
    print("\nEmployee Details:")
    print(result)
else:
    print("Employee not found.")

# c) List of Developers
print("\nList of Developers:")
print(df[df['Designation'] == "Developer"])