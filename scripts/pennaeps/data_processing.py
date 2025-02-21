import pandas as pd
import numpy as np
import os

processed_csv = "processed_data.csv"
# load existing data if it exists
if os.path.exists(processed_csv):
    existing_df = pd.read_csv(processed_csv)
else:
    existing_df = pd.DataFrame()

# process the new data into a DataFrame, skippin ghte fisrt two rows
file_path = '../../../data/pennaeps/Qualified_Facilities_Report.csv'
new_df = pd.read_csv(file_path, skiprows=2)

print(new_df['PA Certification #'].unique().size)
# filter the data to only include PA
new_df = new_df[new_df['State'] == 'PA']
print(new_df['PA Certification #'].unique().size)

#create new column for year
new_df['Certification Start Date'] = pd.to_datetime(new_df['Certification Start Date'], format = '%m/%d/%Y',errors='coerce')    
new_df['Year'] = new_df['Certification Start Date'].dt.year

print(new_df[['Certification Start Date', 'Year']].head(10))

#drop unnecessary columns
columns_to_drop = ['Facility Name', 'Certification Start Date']
new_df = new_df.drop(columns=columns_to_drop, errors='ignore')

print(new_df.columns)
# combine the new data with the existing data
updated_df = pd.concat([existing_df, new_df], ignore_index=True)

# drop duplicates
updated_df = updated_df.drop_duplicates(subset='PA Certification #')

# save the updated data back to the csv
updated_df.to_csv(processed_csv, index=False)