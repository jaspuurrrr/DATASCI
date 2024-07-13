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

# Step 3: Apply log transformation
streams_log = np.log1p(streams)  # Use np.log1p to handle zeros in the data

# Step 4: Calculate the mean (M) and standard deviation (S) of the log-transformed data
M = np.mean(streams_log)
S = np.std(streams_log)

# Step 5: Plot the histogram of log-transformed data
plt.figure(figsize=(10, 6))
plt.hist(streams_log, bins=100, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Log-Transformed Streams')
plt.xlabel('Log(Number of Streams)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Step 6: Perform binning on the log-transformed data
# Define custom bins for log-transformed data
bins = [M - 3*S, M - 2*S, M - S, M, M + S, M + 2*S, M + 3*S, np.inf]
labels = ['Very Low', 'Low', 'Below Average', 'Average', 'Above Average', 'High', 'Very High']

# Apply custom binning
categories = pd.cut(streams_log, bins=bins, labels=labels, include_lowest=True)

# Add the categories to the original DataFrame
data['streams_category'] = categories

# Print a sample of the categorized data
print(data[['streams', 'streams_category']].head())

# Display the range for each category
for label, lower, upper in zip(labels, bins[:-1], bins[1:]):
    print(f"{label}: {np.expm1(lower):.2f} to {np.expm1(upper):.2f}")

# Plot the histogram with categorized data
plt.figure(figsize=(10, 6))
plt.hist(streams_log, bins=bins, color='blue', edgecolor='black', alpha=0.7)
plt.title('Categorized Log-Transformed Streams')
plt.xlabel('Log(Number of Streams)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
