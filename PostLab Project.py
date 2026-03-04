# Smart Home Energy Consumption Monitor

def calculate_current(voltage, resistance):
    return voltage / resistance

def calculate_power(voltage, current):
    return voltage * current

file = open("Daily_Consumption_Report.txt", "w")

num = int(input("Enter number of appliances: "))

file.write("------ Daily Consumption Report ------\n")

for i in range(num):
    name = input("\nEnter Appliance Name: ")
    voltage = float(input("Enter Voltage (V): "))
    resistance = float(input("Enter Resistance (Ohms): "))
    
    current = calculate_current(voltage, resistance)
    power = calculate_power(voltage, current)
    
    print(f"\nAppliance: {name}")
    print(f"Current: {current:.2f} A")
    print(f"Power: {power:.2f} W")
    
    file.write(f"Appliance: {name}\n")
    file.write(f"Voltage: {voltage} V\n")
    file.write(f"Resistance: {resistance} Ohms\n")
    file.write(f"Current: {current:.2f} A\n")
    file.write(f"Power: {power:.2f} W\n")
    
    if power > 1000:
        print("!!! High Power Consumption Appliance !!!")
        file.write("Status: High Power Appliance\n")
        file.write("Suggestion: Limit usage or use energy-efficient model.\n")
    else:
        file.write("Status: Normal Power Appliance\n")
    
    file.write("\n")

file.write("\nGeneral Energy Saving Tips:\n")
file.write("- Turn off appliances when not in use.\n")
file.write("- Use LED bulbs.\n")
file.write("- Use energy-efficient appliances.\n")
file.write("- Avoid overloading circuits.\n")

file.close()

# Reading and Printing File Content
print("\n\n")
read_file = open("Daily_Consumption_Report.txt", "r")
content = read_file.read()
print(content)
read_file.close()

print("\nReport Generated Successfully\nThank You\n\n")