import pandas as pd
import numpy as np
import os

processed_csv = "processed_data.csv"
# load existing data if it exists
if os.path.exists(processed_csv):
    existing_data = pd.read_csv(processed_csv)
else:
    existing_data = pd.DataFrame()

# process the new data into a DataFrame, skippin ghte fisrt two rows
file_path = '../../../data/pennaeps/Qualified_Facilities_Report.csv'
df = pd.read_csv(file_path, skiprows=2)

# display the first few rows of the DataFrame
print('First few rows of the data: ')
print(df.head(5))

print('---------------------------------------------------')
# get an overview of the data
print('Data overview: ')
print(df.info())

print('---------------------------------------------------')
# check basic statistics of the data
print('Basic statistics of the data: ')
print(df.describe())

print('---------------------------------------------------')

# get column labels
print('Column labels: ')
print(df.columns)

print('---------------------------------------------------')

#get unique values in the 'State' column 
print('Unique values in the State column: ')
print(df['State'].unique())
print('---------------------------------------------------')

print('Drop all sataes except PA')
df = df[df['State'] == 'PA']
print(df['State'].unique())


