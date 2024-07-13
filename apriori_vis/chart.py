# Re-running the full code snippet including the file path

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/Users/jaspuurrrr/DATASCI/rank_movement_binned.csv'
dataset = pd.read_csv(file_path)

# Filter the dataset for the year 2019
dataset_2019 = dataset[dataset['year'] == 2019]

# Aggregate the total streams per artist in 2019
artist_streams_2019 = dataset_2019.groupby('artist_names')['streams'].sum().reset_index()

# Convert streams to numeric
artist_streams_2019['streams'] = pd.to_numeric(artist_streams_2019['streams'], errors='coerce')

# Sort by streams in descending order and get the top 10 artists
top_artists_2019 = artist_streams_2019.sort_values(by='streams', ascending=False).head(10)

# Plot the top 10 most streamed artists in 2019
plt.figure(figsize=(12, 8))
plt.barh(top_artists_2019['artist_names'], top_artists_2019['streams'], color='skyblue')
plt.xlabel('Total Streams')
plt.title('Top 10 Most Streamed Artists in 2019')
plt.gca().invert_yaxis()  # To display the highest value at the top
plt.show()




# Filter the dataset for the year 2020
dataset_2020 = dataset[dataset['year'] == 2020]

# Aggregate the total streams per artist in 2020
artist_streams_2020 = dataset_2020.groupby('artist_names')['streams'].sum().reset_index()

# Convert streams to numeric
artist_streams_2020['streams'] = pd.to_numeric(artist_streams_2020['streams'], errors='coerce')

# Sort by streams in descending order and get the top 10 artists
top_artists_2020 = artist_streams_2020.sort_values(by='streams', ascending=False).head(10)

# Plot the top 10 most streamed artists in 2020 with a different color
plt.figure(figsize=(12, 8))
plt.barh(top_artists_2020['artist_names'], top_artists_2020['streams'], color='lightcoral')
plt.xlabel('Total Streams')
plt.title('Top 10 Most Streamed Artists in 2020')
plt.gca().invert_yaxis()  # To display the highest value at the top
plt.show()






# Filter the dataset for the year 2021
dataset_2021 = dataset[dataset['year'] == 2021]

# Aggregate the total streams per artist in 2021
artist_streams_2021 = dataset_2021.groupby('artist_names')['streams'].sum().reset_index()

# Convert streams to numeric
artist_streams_2021['streams'] = pd.to_numeric(artist_streams_2021['streams'], errors='coerce')

# Sort by streams in descending order and get the top 10 artists
top_artists_2021 = artist_streams_2021.sort_values(by='streams', ascending=False).head(10)

# Plot the top 10 most streamed artists in 2021 with a different color
plt.figure(figsize=(12, 8))
plt.barh(top_artists_2021['artist_names'], top_artists_2021['streams'], color='lightgreen')
plt.xlabel('Total Streams')
plt.title('Top 10 Most Streamed Artists in 2021')
plt.gca().invert_yaxis()  # To display the highest value at the top
plt.show()



# Filter the dataset for the year 2022
dataset_2022 = dataset[dataset['year'] == 2022]

# Aggregate the total streams per artist in 2022
artist_streams_2022 = dataset_2022.groupby('artist_names')['streams'].sum().reset_index()

# Convert streams to numeric
artist_streams_2022['streams'] = pd.to_numeric(artist_streams_2022['streams'], errors='coerce')

# Sort by streams in descending order and get the top 10 artists
top_artists_2022 = artist_streams_2022.sort_values(by='streams', ascending=False).head(10)

# Plot the top 10 most streamed artists in 2022 with a different color
plt.figure(figsize=(12, 8))
plt.barh(top_artists_2022['artist_names'], top_artists_2022['streams'], color='lightblue')
plt.xlabel('Total Streams')
plt.title('Top 10 Most Streamed Artists in 2022')
plt.gca().invert_yaxis()  # To display the highest value at the top
plt.show()




# Filter the dataset for the year 2023
dataset_2023 = dataset[dataset['year'] == 2023]

# Aggregate the total streams per artist in 2023
artist_streams_2023 = dataset_2023.groupby('artist_names')['streams'].sum().reset_index()

# Convert streams to numeric
artist_streams_2023['streams'] = pd.to_numeric(artist_streams_2023['streams'], errors='coerce')

# Sort by streams in descending order and get the top 10 artists
top_artists_2023 = artist_streams_2023.sort_values(by='streams', ascending=False).head(10)

# Plot the top 10 most streamed artists in 2023 with a different color
plt.figure(figsize=(12, 8))
plt.barh(top_artists_2023['artist_names'], top_artists_2023['streams'], color='lightpink')
plt.xlabel('Total Streams')
plt.title('Top 10 Most Streamed Artists in 2023')
plt.gca().invert_yaxis()  # To display the highest value at the top
plt.show()