import pandas as pd

# File path of the merged CSV file with dates
input_file = 'merged_2019-2024_with_dates.csv'

# Read the merged CSV file
merged_df = pd.read_csv(input_file)

# Find the maximum number of artists in any row
max_artists = merged_df['artist_names'].apply(lambda x: len(str(x).split(','))).max()

# Split the artist_names column into multiple columns
artist_columns = [f'artist_{i+1}' for i in range(max_artists)]
split_artists = merged_df['artist_names'].str.split(',', expand=True)
merged_df[artist_columns] = split_artists

# Save the updated dataframe to a new CSV file
output_file = 'merged_2019-2024_with_artists.csv'
merged_df.to_csv(output_file, index=False, encoding='utf-8')

print(f'Merged CSV with artists saved as {output_file}')
