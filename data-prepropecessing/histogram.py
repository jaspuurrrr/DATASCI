import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the data from the CSV file
file_path = '/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists.csv'
data = pd.read_csv(file_path, low_memory=False)

# Step 2: Extract the "streams" column
streams = data['streams'].dropna()  # Drop any missing values

# Convert the "streams" column to a numpy array
streams = streams.to_numpy()

# Step 3: Plot a histogram
plt.figure(figsize=(10, 6))
plt.hist(streams, bins=100, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Streams')
plt.xlabel('Number of Streams')
plt.ylabel('Frequency')
plt.grid(True)

# Show the plot
plt.show()
