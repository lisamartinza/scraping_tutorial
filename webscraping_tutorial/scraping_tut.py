import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the webpage
url = "https://tools.sars.gov.za/rex/Rates/Default.aspx"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the table
table = soup.find('table', {'class': 'table table-bordered gvExt'})

# Prepare lists to store the extracted data
countries = []
abbreviations = []
currencies = []
rates = []

# Loop through each row in the table
for row in table.find_all('tr')[1:]:  # Skip the header row, tr = table row
    cells = row.find_all('td') # td = table data, so get all cells in the row
    country = cells[1].text.strip() # country is in the first cell
    abbreviation = cells[2].text.strip() # abbreviation is in the second cell
    currency = cells[3].text.strip() # currency is in the third cell
    rate = float(cells[4].text.strip()) # rate is in the fourth cell
    
    # Append the data to the lists
    countries.append(country)
    abbreviations.append(abbreviation)
    currencies.append(currency)
    rates.append(rate)

# Create a DataFrame
df = pd.DataFrame({
    'Country': countries,
    'Abbreviation': abbreviations,
    'Currency': currencies,
    'Rate': rates
})

# Display the DataFrame
print(df)

# Save the DataFrame to a JSON file
df.to_json('exchange_rates.json', orient='records', indent=4)

print("Data has been saved to exchange_rates.json")