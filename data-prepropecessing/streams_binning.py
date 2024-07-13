import pandas as pd
"""
# File paths
input_file = '/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists.csv'
output_file = '/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists_with_levels.csv'

# Load the data
data = pd.read_csv(input_file, low_memory=False)

# Define bins and labels
bins = [0, 500000, 750000, 1250000, 2000000, 3500000, 5500000, 10000000, float('inf')]
labels = ['Very Low', 'Low', 'Below Average', 'Average', 'Above Average', 'High', 'Very High', 'Extremely High']

# Add stream_level column based on bins
data['stream_level'] = pd.cut(data['streams'], bins=bins, labels=labels, include_lowest=True)

# Define the position to insert the new column (index starts from 0)
insert_position = 9  # Insert between the 10th and 11th column

# Insert stream_level column at the specified position
#data.insert(loc=insert_position, column='stream_level', value=data['stream_level'])

# Drop the original stream_level column (if needed)
# data.drop(columns=['stream_level'], inplace=True)

# Print sample of the updated DataFrame
print(data.head())

# Save the updated DataFrame to a new CSV file
data.to_csv(output_file, index=False)

print(f"New CSV file saved with stream levels: {output_file}")


import pandas as pd

"""

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists_with_levels.csv')

# Define the new order of columns
new_order = ['rank', 'uri', 'artist_names', 'track_name', 'source', 
             'peak_rank', 'previous_rank', 'days_on_chart', 'streams', 
             'stream_level', 'date', 'month', 'year', 'artist_1', 'artist_2', 
             'artist_3', 'artist_4', 'artist_5', 'artist_6', 'artist_7', 
             'artist_8', 'artist_9', 'artist_10', 'artist_11', 'artist_12', 
             'artist_13', 'artist_14', 'artist_15', 'artist_16', 'artist_17', 
             'artist_18']

# Reorder columns
df = df[new_order]

# Remove stream_level from the end
#df.drop(columns=['stream_level'], inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv('/Users/jaspuurrrr/DATASCI/binned_streams.csv', index=False)

