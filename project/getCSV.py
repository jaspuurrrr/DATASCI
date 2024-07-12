import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Set up Chrome options

chrome_options = Options()
chrome_options.add_argument("user-data-dir=/Users/jaspuurrrr/Library/Application Support/Google/Chrome")
chrome_options.add_argument("profile-directory=Profile 8")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": r"\Users\jaspuurrrr\DATASCI\spotify_charts",  # Change default directory for downloads
    "download.prompt_for_download": False,  # Disable download prompt
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Specify the path to the ChromeDriver
chromedriver_path = '/usr/local/bin/chromedriver'

# Create a new Chrome service
service = Service(chromedriver_path)

# Create a new Chrome session
driver = webdriver.Chrome(service=service, options=chrome_options)

# Create folder to store CSV files
folder_path = '/Users/jaspuurrrr/DATASCI/spotify_charts'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Define start and end dates
start_date = datetime(2023, 2, 19)
end_date = datetime(2024, 5, 31)

#__next > div > div > main > div.Content-sc-1n5ckz4-0.jyvkLv > div > header > div > div.ChartsHomeHeader__HeaderLinks-vilr39-2.hQLnwL > a > div.ButtonInner-sc-14ud5tc-0.iMWZgy.encore-bright-accent-set
driver.get("https://charts.spotify.com/home")
time.sleep(5)


# Loop through each day and download the corresponding CSV
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    url = f"https://charts.spotify.com/charts/view/regional-global-daily/{date_str}"
    driver.get(url)

    try:
        # Wait until the download button is clickable
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > div > div > main > div.Content-sc-1n5ckz4-0.jyvkLv > div:nth-child(3) > div > div > a > button'))
        )
        
        # Click the download button
        download_button.click()
        
        # Wait for the download to complete (if necessary)
        # time.sleep(2.5)  # You may need to uncomment this if the download requires a wait
        
        # Move the downloaded file to the specified folder
        download_path = os.path.join(folder_path, 'regional-global-daily.csv')
        destination_path = os.path.join(folder_path, f'{date_str}.csv')
        
        if os.path.exists(download_path):
            os.rename(download_path, destination_path)
            print(f"Downloaded: {date_str}.csv")
        else:
            print(f"Download failed for {date_str}.csv")
    
    except Exception as e:
        print(f"Error on {date_str}: {e}")
    
    current_date += timedelta(days=1)

# Quit the browser session
driver.quit()
