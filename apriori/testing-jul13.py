import time
import numpy as np
import pandas as pd
from efficient_apriori import apriori
import seaborn as sns
import matplotlib.pyplot as plt

start_time = time.time()

# Load data
data = pd.read_csv('/Users/jaspuurrrr/DATASCI/rank_movement_binned.csv', low_memory=False)

# Transform artist_names to list of artists
data['artist_names'] = data['artist_names'].str.split(', ')

# Explode the DataFrame by artist_names
df_artists = data.explode('artist_names').reset_index(drop=True)

# Convert to transaction format (group by track_name and collect artists)
transaction_data = df_artists.groupby(['uri', 'date'])['artist_names'].apply(list).reset_index()
transaction_data = transaction_data.merge(data.drop(columns='artist_names').drop_duplicates(), on=['uri', 'date'])

# Create transactions
transactions = []
for _, row in transaction_data.iterrows():
    values = [
        row['rank_level'],
        row['rank_movement_level'],
        row['track_name'],
        row['stream_level'],
        row['month']
    ]
    
    # Append artists
    for artist in row['artist_names']:
        values.append(f"artist_{artist}")
    
    transactions.append(tuple(values))

# Perform Apriori algorithm
itemsets, rules = apriori(transactions, min_support=0.0001, min_confidence=0.2)

# Create a function to filter and extract relevant columns
def filter_relevant_rules(rules):
    filtered_rules = []
    for rule in rules:
        lhs = [item for item in rule.lhs if item.split('_')[0] in {'rank_level', 'rank_movement_level', 'track_name', 'stream_level', 'month', 'artist'}]
        rhs = [item for item in rule.rhs if item.split('_')[0] in {'rank_level', 'rank_movement_level', 'track_name', 'stream_level', 'month', 'artist'}]
        if lhs and rhs:
            filtered_rules.append((lhs, rhs, rule.lift, rule.confidence))
    return filtered_rules

# Filter rules
filtered_rules = filter_relevant_rules(rules)

# Extract columns and create a DataFrame for lift and confidence
columns = ['rank_level', 'rank_movement_level', 'track_name', 'stream_level', 'month', 'artist_names']
lift_data = pd.DataFrame(0, index=columns, columns=columns, dtype=float)
confidence_data = pd.DataFrame(0, index=columns, columns=columns, dtype=float)

for lhs, rhs, lift, confidence in filtered_rules:
    for l in lhs:
        for r in rhs:
            l_col = l.split('_')[0]
            r_col = r.split('_')[0]
            if l_col in columns and r_col in columns:
                lift_data.at[l_col, r_col] = lift
                confidence_data.at[l_col, r_col] = confidence

# Plot heatmaps for lift and confidence
plt.figure(figsize=(12, 8))
sns.heatmap(lift_data, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Lift Correlation Matrix')
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(confidence_data, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Confidence Correlation Matrix')
plt.show()

end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))
