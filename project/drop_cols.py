import pandas as pd

# Path to your CSV file
csv_file = '/Users/jaspuurrrr/DATASCI/binned_rank_streams.csv'

# Read the CSV into a pandas DataFrame
df = pd.read_csv(csv_file)

# List of columns to drop
columns_to_drop = ['artist_1', 'artist_2', 'artist_3', 'artist_4', 'artist_5',
                   'artist_6', 'artist_7', 'artist_8', 'artist_9', 'artist_10',
                   'artist_11', 'artist_12', 'artist_13', 'artist_14', 'artist_15',
                   'artist_16', 'artist_17', 'artist_18']

# Drop the specified columns
df = df.drop(columns=columns_to_drop)

# Path to save the modified CSV file
output_csv_file = '/Users/jaspuurrrr/DATASCI/binned_rank_streams_updated.csv'

# Write the modified DataFrame to CSV
df.to_csv(output_csv_file, index=False)

print(f"Columns removed and saved to {output_csv_file}")
