# import libraries
import streamlit as st
import pandas as pd
import requests
import json

# https://github.com/lisamartinza/scraping_tutorial/blob/main/exchange_rates.json
url = "https://raw.githubusercontent.com/lisamartinza/scraping_tutorial/main/exchange_rates.json"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

# create dropdown
st.title("Currency to ZAR Converter")

currencies = df['Currency'].tolist()
selected_currency = st.selectbox("Select a currency", currencies)

# input field
amount = st.number_input(f"Enter amount in {selected_currency}", min_value=0.0)

# conversion calculation
if selected_currency:
    rate = df.loc[df['Currency'] == selected_currency, 'Rate'].values[0]
    equivalent_in_rands = amount / rate
    st.write(f"{amount} {selected_currency} is equivalent to {equivalent_in_rands:.2f} ZAR")

# run the app in terminal
#streamlit run app.py