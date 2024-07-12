import pandas as pd
from apyori import apriori

# Load the CSV file
file_path = '/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists.csv'
data = pd.read_csv(file_path)

# Extract columns related to artist names
artist_columns = [f'artist_{i}' for i in range(1, 19)]
artist_data = data[artist_columns]

# Fill NaN values with an empty string and convert to list of lists
artist_data = artist_data.fillna('')
artist_lists = artist_data.values.tolist()

# Remove empty strings from each list
artist_lists = [[artist for artist in track if artist] for track in artist_lists]

# Apply the Apriori algorithm
min_support = 0.01
min_confidence = 0.2
min_lift = 2

association_rules = list(apriori(artist_lists, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift))

# Display the first few association rules
for rule in association_rules[:5]:
    print(rule)
