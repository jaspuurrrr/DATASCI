import pandas as pd

# Step 1: Read the CSV file
file_path = '/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists_copy.csv'  # replace with your file path
df = pd.read_csv(file_path)

# Step 2: Keep only the first 100 rows
df_first_100 = df.iloc[:10, :12]

# Step 3: Save the new DataFrame to a CSV file
output_path = '/Users/jaspuurrrr/DATASCI/sample.csv'  # replace with your desired output path
df_first_100.to_csv(output_path, index=False)

print("The first 100 rows have been saved to the new CSV file.")
