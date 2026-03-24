# Smart Home Energy Consumption Monitor
# The Challenge: Simulate a smart meter that reads voltage (V) and resistance (R)
# for various home appliances. Calculate current (I) and Power (P). Use Control
# Flow to identify high-power appliances and File Handling to generate a "Daily
# Consumption Report" that suggests ways to save electricity.

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

print("Report Displayed Successfully!")





# ------------------------------------------------OUTPUT:------------------------------------------------


# Enter number of appliances: 2

# Enter Appliance Name: Fan
# Enter Voltage (V): 29
# Enter Resistance (Ohms): 200

# Appliance: Fan
# Current: 0.14 A
# Power: 4.21 W

# Enter Appliance Name: AC
# Enter Voltage (V): 20
# Enter Resistance (Ohms): 300

# Appliance: AC
# Current: 0.07 A
# Power: 1.33 W



# ------ Daily Consumption Report ------
# Appliance: Fan
# Voltage: 29.0 V
# Resistance: 200.0 Ohms
# Current: 0.14 A
# Power: 4.21 W
# Status: Normal Power Appliance

# Appliance: AC
# Voltage: 20.0 V
# Resistance: 300.0 Ohms
# Current: 0.07 A
# Power: 1.33 W
# Status: Normal Power Appliance


# General Energy Saving Tips:
# - Turn off appliances when not in use.
# - Use LED bulbs.
# - Use energy-efficient appliances.
# - Avoid overloading circuits.

# Report Displayed Successfully!