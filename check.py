import os
from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime.strptime('19-01-01', '%y-%m-%d')
end_date = datetime.strptime('24-05-31', '%y-%m-%d')

# Define the folder path
folder_path = "spotify_charts"

# Function to check if file exists for a given date
def check_file_existence(date):
    filename = f"regional-global-daily-{date}.csv"
    filepath = os.path.join(folder_path, filename)
    if not os.path.exists(filepath):
        print(f"{filename} does not exist in the folder.")

# Loop through each date and check file existence
current_date = start_date
while current_date <= end_date:
    check_file_existence(current_date.strftime('%Y-%m-%d'))
    current_date += timedelta(days=1)
