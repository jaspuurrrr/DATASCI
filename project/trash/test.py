import time
import pandas as pd
import io
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Specify the path to your chromedriver executable
chromedriver_path = '/usr/local/bin/chromedriver'  # Update with your actual path

# Function to fetch the CSV data from Spotify Charts using Selenium
def fetch_csv(date):
    url = f"https://charts.spotify.com/charts/view/regional-global-daily/{date}"
    
    # Setup Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Optional: Run Chrome in headless mode
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    driver.get(url)
    
    try:
        # Wait for the download button to be clickable with a timeout of 10 seconds
        wait = WebDriverWait(driver, 10)
        download_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Button-me270r-0 fFXuoY"))
        )
        
        # Click the download button
        download_button.click()
        
        # Wait a few seconds for download to complete (adjust as needed)
        time.sleep(5)
        
        # Assume the file is downloaded to a default location or to a known location
        csv_filename = f"spotify_charts_{date}.csv"  # Adjust filename if needed
        
        # Read the downloaded CSV file
        with open(csv_filename, 'r', encoding='utf-8') as f:
            csv_content = f.read()
        
        return csv_content
        
    except TimeoutException as e:
        print(f"Timeout waiting for download button to be clickable: {e}")
        return None  # Return None if there's a timeout
    
    except Exception as e:
        print(f"Failed to fetch CSV data for {date}: {e}")
        return None
    
    finally:
        driver.quit()

# Function to process the CSV data and add date columns
def process_csv(date_str, csv_content):
    if csv_content is None:
        return None
    
    date = datetime.strptime(date_str, "%Y-%m-%d")
    df = pd.read_csv(io.StringIO(csv_content))
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
            if csv_content is not None:
                daily_df = process_csv(date_str, csv_content)
                if daily_df is not None:
                    combined_df = pd.concat([combined_df, daily_df], ignore_index=True)
                    print(f"Processed data for {date_str}")
                else:
                    print(f"No data processed for {date_str}")
            else:
                print(f"Failed to fetch CSV data for {date_str}")
        
        except Exception as e:
            print(f"Failed to process data for {date_str}: {e}")
        
        current_date += timedelta(days=1)
    
    if not combined_df.empty:
        combined_df.to_csv("combined_spotify_charts.csv", index=False)
        print("Combined CSV saved as combined_spotify_charts.csv")
    else:
        print("No data to save.")

# Define the date range
start_date = datetime(2019, 1, 1)
end_date = datetime(2024, 5, 31)

# Run the script
combine_csvs(start_date, end_date)
