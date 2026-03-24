import pandas as pd

# Create data for 5 states
data = {
    'State': ['Maharashtra', 'Gujarat', 'Karnataka', 'Rajasthan', 'Punjab'],
    'Area': [307713, 196244, 191791, 342239, 50362],   # in sq km
    'Population': [112374333, 60439692, 61095297, 68548437, 27743338]
}

df = pd.DataFrame(data)

# a) Complete information
print("\n--- State Information ---")
print(df)

# b) State with largest area
largest_area = df.loc[df['Area'].idxmax()]
print("\nState with largest area:", largest_area['State'])

# c) State with largest population
largest_pop = df.loc[df['Population'].idxmax()]
print("State with largest population:", largest_pop['State'])

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']

print("\nPopulation Density:")
print(df[['State', 'Density']])

# e) State with highest density
highest_density = df.loc[df['Density'].idxmax()]
print("\nState with highest population density:", highest_density['State'])