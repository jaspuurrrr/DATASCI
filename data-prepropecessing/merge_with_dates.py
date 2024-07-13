import pandas as pd
import os
from datetime import datetime

# Define the folder containing the CSV files
folder_path = '/Users/jaspuurrrr/DATASCI/spotify_charts'

# Create an empty list to store dataframes
dfs = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        # Extract date, month, and year from the filename
        date_str = '-'.join(filename.split('-')[-3:]).split('.')[0]
        date = datetime.strptime(date_str, '%Y-%m-%d')
        year = date.year
        month = date.strftime('%B')
        
        # Try reading with UTF-8 encoding first
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            # Fallback to ISO-8859-1 encoding if UTF-8 fails
            df = pd.read_csv(file_path, encoding='ISO-8859-1')
        
        # Add the new columns to the dataframe
        df['date'] = date_str
        df['month'] = month
        df['year'] = year
        
        # Append the dataframe to the list
        dfs.append(df)

# Concatenate all dataframes in the list
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged dataframe to a new CSV file
output_file = 'merged_2019-2024_with_dates.csv'
merged_df.to_csv(output_file, index=False, encoding='utf-8')

print(f'Merged CSV saved as {output_file}')
