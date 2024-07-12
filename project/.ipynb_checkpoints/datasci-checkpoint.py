import requests
import pandas as pd
from datetime import datetime, timedelta

# Function to fetch the CSV data from Spotify Charts
def fetch_csv(date):
    url = f"https://charts.spotify.com/charts/view/regional-global-daily/{date}"
    response = requests.get(url)
    response.raise_for_status()
    
    # Find the CSV link in the response text
    start_index = response.text.find("href=\"") + 6
    end_index = response.text.find("\"", start_index)
    csv_url = response.text[start_index:end_index]
    
    # Fetch the CSV content
    csv_response = requests.get(csv_url)
    csv_response.raise_for_status()
    return csv_response.content.decode('utf-8')

# Function to process the CSV data and add date columns
def process_csv(date_str, csv_content):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    df = pd.read_csv(pd.compat.StringIO(csv_content))
    df['date'] = date.strftime("%Y-%m-%d")
    df['month'] = date.month
    df['year'] = date.year
    return df

# Main function to combine all CSVs from a date range
def combine_csvs(start_date, end_date):
    current_date = start_date
    combined_df = pd.DataFrame()
    
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        try:
            csv_content = fetch_csv(date_str)
            daily_df = process_csv(date_str, csv_content)
            combined_df = pd.concat([combined_df, daily_df], ignore_index=True)
            print(f"Processed data for {date_str}")
        except Exception as e:
            print(f"Failed to process data for {date_str}: {e}")
        
        current_date += timedelta(days=1)
    
    combined_df.to_csv("combined_spotify_charts.csv", index=False)
    print("Combined CSV saved as combined_spotify_charts.csv")

# Define the date range
start_date = datetime(2019, 1, 1)
end_date = datetime(2024, 5, 31)

# Run the script
combine_csvs(start_date, end_date)
