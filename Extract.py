#Imports
import pandas as pd
import requests
from bs4 import BeautifulSoup

def f1_driver_standing():
    # Step 1: Fetch the webpage
    url = 'https://www.formula1.com/en/results/2024/races'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table (replace class names if needed)
    table = soup.find("table", class_="f1-table f1-table-with-data w-full")
    
    headers = []
    
    # Extract the table headers
    for i in table.find_all('th'):
        title = i.text.strip()
        headers.append(title)
    
    # Create a DataFrame with the headers
    f1_table_df = pd.DataFrame(columns=headers)
    
    # Extract the table rows
    for j in table.find_all('tr')[1:]:  # Skip the header row
        row_data = j.find_all('td')
        row = [i.text.strip() for i in row_data]
        length = len(f1_table_df)
        f1_table_df.loc[length] = row
    
    # Print the DataFrame
    print(f1_table_df)
    
    return f1_table_df

# Example usage
df = f1_driver_standing()
