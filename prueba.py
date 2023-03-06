import requests
import streamlit as st


options = [
    "https://api.binance.com",
    "https://api1.binance.com",
    "https://api2.binance.com",
    "https://api3.binance.com",
    "https://api.binance.us",
    "https://data.binance.com",
]

base_endpoint = st.selectbox(label="Base endpoint", options=options)
url = f"{base_endpoint}/api/v3/depth?symbol=BTCBUSD&limit=5"
st.write(url)
response = requests.get(url)
st.write(response.json())
