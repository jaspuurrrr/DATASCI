import time
import numpy as np 
import pandas as pd 
from efficient_apriori import apriori
from tabulate import tabulate
#from apyori import apriori

start_time = time.time()

# Load data
data = pd.read_csv('/Users/jaspuurrrr/DATASCI/binned_rank_streams.csv', low_memory=False) 
data2 = pd.read_csv('/Users/jaspuurrrr/DATASCI/apriori/testing.csv', low_memory=False) 
data.head() 

print("Shape of the data:", data.shape)

df = pd.DataFrame(data)
df['artist_names'] = df['artist_names'].str.split(', ')

df_artists = df.explode('artist_names').reset_index(drop=True)
print("\nDataFrame with artists split into separate rows:")
print(df_artists.head())

# Remove duplicates caused by exploding rows
#df_artists.drop_duplicates(inplace=True)

# Convert to transaction format (group by track_name and collect artists)
transaction_data = df_artists.groupby(['uri', 'date'])['artist_names'].apply(list).reset_index()
transaction_data = transaction_data.merge(df.drop(columns='artist_names').drop_duplicates(), on=['uri', 'date'])

print("\nTransaction format data:")
print(len(transaction_data.head(100)))
print(transaction_data.head(1000))

transactions = []

# Preprocess dataset to replace None with empty string
count = 0
for _, row in transaction_data.head(395487).iterrows():
    count += 1
    values = [
        #row['rank_level'],
        #row['track_name'],
        row['month'],
        #row['date'],
        #row['stream_level'],
        f"artist_{row['artist_1']}"
    ]
    
    # Append artists from artist_2 to artist_18
    for i in range(2, 19):
        artist_col = f'artist_{i}'
        values.append('' if pd.isna(row[artist_col]) else f"artist_{row[artist_col]}")
    
    transactions.append(tuple(values))

#print(transactions)

# Perform Apriori algorithm
records = []
for i in range(0, 20):
    records.append([str(data.values[i, j]) for j in [1, 10, 12]])

print(tabulate(transactions, headers=["month", "stream_level", "artist_1", "artist_2", "artist_3", "artist_4", "artist_5", "artist_6", "artist_7", "artist_8", "artist_9", "artist_10", "artist_11", "artist_12", "artist_13", "artist_14", "artist_15", "artist_16", "artist_17", "artist_18"]))#]))#

itemsets, rules = apriori(transactions, min_support=0.0001, min_confidence=0.2)

# Define a function to check if an item is an artist
def is_artist(item):
    return item.startswith('artist_')

# Filter out rules containing empty strings and ensure no artist is on both sides
filtered_rules = [
    rule for rule in rules
    if all(item != '' for item in rule.lhs) and all(item != '' for item in rule.rhs) and
       not (any(is_artist(item) for item in rule.lhs) and any(is_artist(item) for item in rule.rhs))
]

#filtered_rules = filter(lambda rule: len(rule.lhs) >= 2 and len(rule.rhs) == 1, rules)

print(len(filtered_rules))
# Print the filtered association rules sorted by confidence
for rule in sorted(filtered_rules, key=lambda rule: rule.confidence):
    print(rule)


end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))


"""
start_time = time.time()

records = []
for i in range(0, 100):
    records.append([str(data.values[i, j]) for j in [0, 1, 3, 4, 10, 12, 13]])




itemsets, rules = apriori(records, min_support=0.005, min_confidence=0.2)

# Filter rules where lhs has 2 items and rhs has 1 item
filtered_rules = filter(lambda rule: len(rule.lhs) >= 3 and len(rule.rhs) == 1, rules)

# Sort and print the rules by lift
for rule in sorted(filtered_rules, key=lambda rule: rule.lift):
    print(rule)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))

"""
