import pandas as pd
import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse('response.xml')
root = tree.getroot()

# Define dataframe columns
columns = ["Race", "Number of Deaths", "Population", "Crude Death Rate",
           "Age Adjusted Death Rate", "Confidence Interval", "Standard Error"]

# Initialize empty list to store rows
rows = []

# Initialize year variable
years = []

# Loop through each row in the XML data
for j, row in enumerate(root.findall('.//r')):
    # Extract data from each column in the row
    data = []
    for i, col in enumerate(row.findall('c')):
        if 'l' in col.attrib:
            # If it's the first column, it represents the year
            if (j % 5 == 0) and i == 0:
                year = col.attrib['l']
                # Append the year to the years list
                years.append(year)
            else:
                data.append(col.attrib['l'])
        elif 'v' in col.attrib:
            data.append(col.attrib['v'])
        elif 'a' in col.attrib:
            data.append(col.attrib['a'])
            # Extract confidence interval
            limit = col.find('l')
            if limit is not None:
                data.append(limit.attrib['v'])
        elif 'dt' in col.attrib:
            data.append(col.attrib['dt'])

    # If it's not a subtotal row, add year to data and append it to the list
    if 'c' not in col.attrib:
        rows.append(data)

# Create a dataframe from the list of rows
df = pd.DataFrame(rows, columns=columns)
long_years = []

for i in years:
    for l in range(5):
        long_years.append(i)
long_years.append(0)
# print(long_years)
df['year'] = long_years


# Create a boolean mask for rows where 'Race' column starts with a number
mask = df['Race'].str.startswith(tuple('0123456789'))

# Create a new dataframe with the rows where 'Race' starts with a number
summary_df = df[mask]

# Remove those rows from the original dataframe
df = df[~mask]

print(df.head(10))

df.reset_index(inplace = True)
df.drop(columns = 'index', inplace = True)
df.to_pickle('my_df.pkl')