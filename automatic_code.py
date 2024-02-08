import pandas as pd
import webbrowser

# Function to open URL in Chrome
def open_url_in_chrome(url):
    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'  # Path to Chrome executable
    webbrowser.get(chrome_path).open(url)

# Read Excel file
excel_file = '"C:\Users\SUVAJIT\Desktop\python.xlsx"'  # Change this to your Excel file path
df = pd.read_excel(excel_file)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    url = row['URL']
    print(f"Opening URL: {url}")
    open_url_in_chrome(url)
    
    # Prompt for keyboard input to proceed to the next URL
    input("Press any key to open next URL...")

print("All URLs have been opened.")

	