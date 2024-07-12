import pandas as pd

# File paths
input_file = '/Users/jaspuurrrr/DATASCI/binned_rank_streams_peak.csv'
output_file = '/Users/jaspuurrrr/DATASCI/binned_rank_streams_peak_prev.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/jaspuurrrr/DATASCI/binned_rank_streams_peak.csv', low_memory=False)

# Define ranges and corresponding labels
ranges = [1, 2, 6, 11, 21, 51, 101, 151, 201]
labels = ['Prev Top 1', 'Prev Top 5', 'Prev Top 10', 'Prev Top 20', 'Prev Top 50', 'Prev Top 100', 'Prev Top 150', 'Prev Top 200']

# Use pd.cut to create the new column based on ranges and labels
df['previous_rank_level'] = pd.cut(df['previous_rank'], bins=ranges, labels=labels, right=False)

# Define the new order of columns
new_order = ['rank', 'rank_level',  'uri', 'artist_names', 'track_name', 'source', 
             'peak_rank', 'peak_rank_level', 'previous_rank', 'previous_rank_level', 'days_on_chart', 'streams', 
             'stream_level', 'date', 'month', 'year', 'artist_1', 'artist_2', 
             'artist_3', 'artist_4', 'artist_5', 'artist_6', 'artist_7', 
             'artist_8', 'artist_9', 'artist_10', 'artist_11', 'artist_12', 
             'artist_13', 'artist_14', 'artist_15', 'artist_16', 'artist_17', 
             'artist_18']

# Reorder columns
df = df[new_order]

# Display the updated DataFrame
print(df[['previous_rank', 'previous_rank_level']].head(20))  # Displaying first 10 rows of 'rank' and 'rank_levels'

df.to_csv('/Users/jaspuurrrr/DATASCI/binned_rank_streams_peak_prev.csv', index=False)