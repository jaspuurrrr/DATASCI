import pandas as pd
import numpy as np

# File paths
input_file = '/Users/jaspuurrrr/DATASCI/binned_rank_streams_peak_prev.csv'
output_file = '/Users/jaspuurrrr/DATASCI/binned_rank_streams_peak_prev_days.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file, low_memory=False)

# Define ranges and corresponding labels
ranges = [0,5,23,105,475,2141, np.inf]
labels = ['Newcomer', 'Short-term', 'Moderate-term', 'Mid-term', 'Long-term', 'Extended-term']

# Use pd.cut to create the new column based on ranges and labels
df['days_on_chart_level'] = pd.cut(df['days_on_chart'], bins=ranges, labels=labels, right=False)

# Define the new order of columns
new_order = ['rank', 'rank_level',  'uri', 'artist_names', 'track_name', 'source', 
             'peak_rank', 'peak_rank_level', 'previous_rank', 'previous_rank_level', 'days_on_chart', 'days_on_chart_level', 'streams', 
             'stream_level', 'date', 'month', 'year', 'artist_1', 'artist_2', 
             'artist_3', 'artist_4', 'artist_5', 'artist_6', 'artist_7', 
             'artist_8', 'artist_9', 'artist_10', 'artist_11', 'artist_12', 
             'artist_13', 'artist_14', 'artist_15', 'artist_16', 'artist_17', 
             'artist_18']

# Reorder columns
df = df[new_order]

# Display the updated DataFrame
print(df[['days_on_chart', 'days_on_chart_level']].head(100))  # Displaying first 10 rows of 'rank' and 'rank_levels'

df.to_csv(output_file, index=False)