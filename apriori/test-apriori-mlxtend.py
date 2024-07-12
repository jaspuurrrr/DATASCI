import time
import numpy as np
import pandas as pd
from datetime import datetime
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_csv('/Users/jaspuurrrr/DATASCI/binned_rank_streams.csv', low_memory=False)
data.head()

print("Shape of the data:", data.shape)

start_time = time.time()
start_time_readable = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
print(str(start_time_readable) + "\n")

records = []
for i in range(0, 100):
    records.append([str(data.values[i, j]) for j in [0, 1, 3, 4, 10, 12, 13]])

df_records = pd.DataFrame(records)
df_records = pd.get_dummies(df_records)

frequent_itemsets = apriori(df_records, min_support=0.005, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)

filtered_rules = rules[(rules['antecedents'].apply(len) >= 3) & (rules['consequents'].apply(len) == 1)]

filtered_rules = filtered_rules.sort_values(by='lift', ascending=True)

for _, rule in filtered_rules.iterrows():
    print(f"Rule: {set(rule['antecedents'])} -> {set(rule['consequents'])}")
    print(f"Support: {rule['support']}, Confidence: {rule['confidence']}, Lift: {rule['lift']}\n")

end_time = time.time()
end_time_readable = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
print(str(start_time_readable) + "\n")
print(str(end_time_readable) + "\n")
execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))
