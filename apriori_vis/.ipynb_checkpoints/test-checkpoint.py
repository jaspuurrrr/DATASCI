import pandas as pd

# Load data from CSV
file_path = '/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists.csv'
df = pd.read_csv(file_path)

# Print column names to identify the correct one containing items
print("Columns in DataFrame:")
print(df.columns)
