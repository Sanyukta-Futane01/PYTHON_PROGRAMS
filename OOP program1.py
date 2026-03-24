class Employee:
    def __init__(self, name="", age=0, salary=0, address=""):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def input_info(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Address: {self.address}")


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def input_info(self):
        super().input_info()
        self.department = input("Enter department: ")

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


# Processing 10 managers
managers = []

for i in range(10):
    print(f"\nEnter details of Manager {i+1}:")
    m = Manager()
    m.input_info()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display_info()