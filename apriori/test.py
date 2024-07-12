'''import time
import numpy as np 
import pandas as pd 
from datetime import datetime
from efficient_apriori import apriori
#from apyori import apriori

data = pd.read_csv('/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists.csv', low_memory=False) 
data.head() 

print("Shape of the data:", data.shape)

start_time = time.time()

records = []
for i in range(0, 100):
    records.append([str(data.values[i, j]) for j in [2, 10, 12]])

end_time1 = time.time()   

print("Execution time: {:.2f} seconds".format(end_time1-start_time))

#print(str(datetime.fromtimestamp(end_time1).strftime('%Y-%m-%d %H:%M:%S')))
#association_rules = apriori(records, min_support=0.001, min_confidence=0.2)
#association_rules = apriori(records, min_support=0.0000001, min_confidence=0.2, min_lift=3, min_length=2)

#association_results = list(association_rules)

#for i in range(min(50, len(association_results))):
#    print(association_results[i])
#    print("\n")


# Apply the apriori algorithm
itemsets, rules = apriori(records, min_support=0.01, min_confidence=0.5)

# Filter rules where lhs has 2 items and rhs has 1 item
filtered_rules = filter(lambda rule: len(rule.lhs) >= 2 and len(rule.rhs) == 1, rules)

# Sort and print the rules by lift
for rule in sorted(filtered_rules, key=lambda rule: rule.lift):
    print(rule)

end_time = time.time()
execution_time = end_time - end_time1
print("Execution time: {:.2f} seconds".format(execution_time))'''

import numpy as np

# Define the prior probabilities
P_i = 0.7
P_h = 0.6

# Define the conditional probability tables (CPTs)
P_t_given_i = {True: 0.8, False: 0.5}
P_u_given_i_h = {
    (True, True): 0.9,
    (True, False): 0.3,
    (False, True): 0.5,
    (False, False): 0.1
}
P_e_given_t_u = {
    (True, True): 0.9,
    (True, False): 0.5,
    (False, True): 0.7,
    (False, False): 0.3
}

# Compute joint probability P(i, h, t, u, e)
def joint_probability(i, h, t, u, e):
    P_t = P_t_given_i[i]
    P_u = P_u_given_i_h[(i, h)]
    P_e = P_e_given_t_u[(t, u)]
    P_ih = P_i if i else (1 - P_i)
    P_h_prob = 0.6 if h else 0.4
    return P_ih * P_h_prob * P_t * P_u * P_e

# Marginalize over i, h, and t to find P(u, e)
def marginalize_uh(u, e):
    total_prob = 0
    for i in [True, False]:
        for h in [True, False]:
            for t in [True, False]:
                total_prob += joint_probability(i, h, t, u, e)
    return total_prob

# Compute P(e)
def compute_P_e(e):
    return marginalize_uh(True, e) + marginalize_uh(False, e)

# Compute P(u|e) = P(u, e) / P(e)
def compute_P_u_given_e(e):
    P_e = compute_P_e(e)
    P_u_e = marginalize_uh(True, e)
    return P_u_e / P_e

# Given that the student did well on the test (e = True)
P_u_given_e = compute_P_u_given_e(True)
print("P(u|e) =", P_u_given_e)
