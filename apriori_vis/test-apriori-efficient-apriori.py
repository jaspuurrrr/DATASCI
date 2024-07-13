import time
import numpy as np 
import pandas as pd 
from efficient_apriori import apriori
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd
import re
#from apyori import apriori

start_time = time.time()

data = pd.read_csv('/Users/jaspuurrrr/DATASCI/rank_movement_binned.csv', low_memory=False) 
data.head() 

df = pd.DataFrame(data)
'''df['artist_names'] = df['artist_names'].str.split(', ')

df_artists = df.explode('artist_names').reset_index(drop=True)

transaction_data = df_artists.groupby(['uri', 'date'])['artist_names'].apply(list).reset_index()
transaction_data = transaction_data.merge(df.drop(columns='artist_names').drop_duplicates(), on=['uri', 'date'])'''


transactions = []

count = 0
for _, row in transaction_data.head(395487).iterrows():
    count += 1
    values = [
        #row['rank_movement_level'],
        #row['track_name'],
        #row['stream_level'],
        f"month_{row['month']}",
        #row['stream_level'],
        f"artist_{row['artist_1']}"
    ]
    
    # Append artists from artist_2 to artist_18
    for i in range(2, 19):
        artist_col = f'artist_{i}'
        values.append('' if pd.isna(row[artist_col]) else f"artist_{row[artist_col]}")
    
    transactions.append(tuple(values))

itemsets, rules = apriori(transactions, min_support=0.0005, min_confidence=0.2)

def is_artist(item):
    return item.startswith('artist_')

def is_month(item):
    return item.startswith('month_')

def table_form(output):
    artists = []
    outcomes = []
    confidences = []
    supports = []
    lifts = []
    convictions = []

    for rule in output.splitlines():
        match = re.match(r'\{(?:[a-z]+_)?(.+?)\} -> \{(?:[a-z]+_)?(.+?)\} \(conf: ([0-9.]+), supp: ([0-9.]+), lift: ([0-9.]+), conv: ([0-9.]+)\)', rule)
        if match:
            artist, outcome, conf, supp, lift, conv = match.groups()
            artists.append(artist)
            outcomes.append(outcome)
            confidences.append(float(conf))
            supports.append(float(supp))
            lifts.append(float(lift))
            convictions.append(float(conv))

    df = pd.DataFrame({
        'Antecedent': artists,
        'Consequent': outcomes,
        'Confidence': confidences,
        'Support': supports,
        'Lift': lifts,
        'Conviction': convictions
    })

    df = df.sort_values(by='Confidence', ascending=True)


    plt.figure(figsize=(12, 6))
    table = plt.table(cellText=df.values,
                      rowLabels=df.index,
                      colLabels=df.columns,
                      cellLoc='center',
                      loc='center')


    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2)

    plt.title('')
    plt.axis('off') 
    plt.show()


filtered_rules = [
    rule for rule in rules
    if all(item != '' for item in rule.lhs) and all(item != '' for item in rule.rhs) and #(any(is_artist(item) and is_month(item) for item in rule.lhs)) and
       not (any(is_artist(item) for item in rule.lhs) and any(is_artist(item) for item in rule.rhs))
]


print(len(filtered_rules))

text = """"""
for rule in sorted(filtered_rules, key=lambda rule: rule.confidence):
    text += str(rule)
    text += "\n"
    #print(rule)

table_form(text)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))
