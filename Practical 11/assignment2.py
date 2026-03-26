import matplotlib.pyplot as plt

# Data
companies = ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "ATOS", "Amdocs"]
recruitments = [120, 150, 180, 100, 90, 130, 80, 110]

# a) Bar Chart
plt.figure()
plt.bar(companies, recruitments)
plt.title("Company Recruitments")
plt.xlabel("Companies")
plt.ylabel("Number of Hires")
plt.xticks(rotation=30)
plt.show()

# b) Pie Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        startangle=140, explode=[0,0.1,0,0,0,0,0,0])
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# e) IBM vs Amdocs Comparison
labels = ["IBM", "Amdocs"]
values = [100, 110]

plt.figure()
plt.bar(labels, values)
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("Number of Hires")
plt.show()