import pandas as pd
import numpy as np

# Step 1: Load the data from the CSV file
file_path = '/Users/jaspuurrrr/DATASCI/merged_2019-2024_with_artists.csv'
data = pd.read_csv(file_path, low_memory=False)

# Step 2: Extract the "streams" column
streams = data['streams'].dropna()  # Drop any missing values

# Convert the "streams" column to a numpy array
streams = streams.to_numpy()

# Step 3: Calculate the mean (M) and standard deviation (S) of the "streams" data
M = np.mean(streams)
S = np.std(streams)

# Step 4: Compute the required values
values = [M - 3*S, M - 2*S, M - S, M, M + S, M + 2*S, M + 3*S]

# Print the results
print("Mean (M):", M)
print("Standard Deviation (S):", S)
print("M-3S, M-2S, M-S, M, M+S, M+2S, M+3S:", values)
