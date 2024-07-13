import pandas as pd

# File paths
input_file = '/Users/jaspuurrrr/DATASCI/rank_movement.csv'
output_file = '/Users/jaspuurrrr/DATASCI/rank_movement_binned.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file, low_memory=False)

# Define ranges and corresponding labels
ranges = [-199, -100, -50, -20, -10, -5, 0, 1, 6, 11, 21, 51, 101, 200]
labels = ['Extreme Decrease', 'Significant Decrease', 'Moderate Decrease', 'Mild Decrease', 
          'Minimal Decrease', 'Very Minimal Decrease', 'No Change', 
          'Very Minimal Increase', 'Minimal Increase', 'Mild Increase', 
          'Moderate Increase', 'Significant Increase', 'Extreme Increase']

# Create a new column 'rank_movement_level' and initialize it with the same values as 'rank_movement'
df['rank_movement_level'] = df['rank_movement']

# Apply binning only to numeric values in 'rank_movement'
numeric_mask = pd.to_numeric(df['rank_movement'], errors='coerce').notnull()
df.loc[numeric_mask, 'rank_movement_level'] = pd.cut(df.loc[numeric_mask, 'rank_movement'].astype(float), bins=ranges, labels=labels, right=False)

# Define the new order of columns
new_order = ['rank', 'rank_level', 'rank_movement', 'rank_movement_level', 'uri', 'artist_names', 'track_name', 'source', 
             'peak_rank', 'peak_rank_level', 'previous_rank', 'previous_rank_level', 'days_on_chart', 'days_on_chart_level', 'streams', 
             'stream_level', 'date', 'month', 'year', 'artist_1', 'artist_2', 
             'artist_3', 'artist_4', 'artist_5', 'artist_6', 'artist_7', 
             'artist_8', 'artist_9', 'artist_10', 'artist_11', 'artist_12', 
             'artist_13', 'artist_14', 'artist_15', 'artist_16', 'artist_17', 
             'artist_18']

# Reorder columns
df = df[new_order]

# Display the updated DataFrame
print(df[['rank_movement', 'rank_movement_level']].head(100))  # Displaying first 100 rows of 'rank_movement' and 'rank_movement_level'

# Save the updated DataFrame to a CSV file
df.to_csv(output_file, index=False)
