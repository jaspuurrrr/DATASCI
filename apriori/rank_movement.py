import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/jaspuurrrr/DATASCI/binned_rank_streams_peak_prev_days.csv')

# Calculate rank_movement
df['rank_movement'] = df.apply(lambda row: "New Entry" if row['previous_rank'] == -1 else row['previous_rank'] - row['rank'], axis=1)

# Insert the rank_movement column at the desired position
position = df.columns.get_loc('rank_level') + 1
df.insert(position, 'rank_movement', df.pop('rank_movement'))

# Save the DataFrame back to a CSV file (optional)
df.to_csv('/Users/jaspuurrrr/DATASCI/rank_movement.csv', index=False)

print(df.head())
