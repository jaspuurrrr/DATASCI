import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from efficient_apriori import apriori

# Load the CSV file
input_file = '/Users/jaspuurrrr/DATASCI/rank_movement_binned.csv'
df = pd.read_csv(input_file, low_memory=False)

# Create transactions from the DataFrame
transactions = df[['month', 'year']].values.tolist()

# Apply the Apriori algorithm
itemsets, rules = apriori(transactions, min_support=0.01, min_confidence=0.5)

# Create a matrix of associations
'''items = list(set([item for sublist in transactions for item in sublist]))
item_index = {item: i for i, item in enumerate(items)}
matrix = np.zeros((len(items), len(items)))'''

# Populate the matrix
for rule in rules:
    print(rule)
    '''
    antecedent = list(rule.lhs)
    consequent = list(rule.rhs)
    for a in antecedent:
        for c in consequent:
            matrix[item_index[a], item_index[c]] = rule.confidence

# Convert to DataFrame for plotting
matrix_df = pd.DataFrame(matrix, index=items, columns=items)

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(matrix_df, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Association Matrix')
plt.show()'''
