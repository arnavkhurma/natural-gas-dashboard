import streamlit as st
import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()
FRED_API_KEY = os.getenv("FRED_API")
base_url = "https://api.stlouisfed.org/fred/"

# FRED PAGE
def load_fred():
    # SIDEBAR
    st.sidebar.header("FRED")
    type = st.sidebar.radio(
        'Type', 
        ['Series (Observations)', 'Series (Plots)']
    )
    endpoint = None
    if type == 'Series (Observations)':
        endpoint = 'series/observations'
    elif type == 'Series (Plots)':
        enpoint = 'series/plots'
    id = st.sidebar.text_input("Series ID", placeholder="Ticker", value=None)
    start = st.sidebar.date_input("From", value=None)
    end = st.sidebar.date_input("To", value=None)
    freq = st.sidebar.radio(
        'Frequency', 
        ['Day', 'Month']
    )
    units = st.sidebar.text_input("Units", placeholder="Units", value=None)
    
    # API
    obs_params = {
        'series_id': id,
        'api_key': FRED_API_KEY,
        'file_type': 'json',
        'observation_start': start,
        'observation_end': end,
        # 'frequency': freq
        # 'units': units
    }
    submit = st.sidebar.button("Submit", type="primary")
    if submit:
        response = requests.get(base_url + endpoint, params=obs_params)
        if response.status_code == 200:
            res_data = response.json()
            obs_data = pd.DataFrame(res_data['observations'])
            obs_data['date'] = pd.to_datetime(obs_data['date'])
            obs_data.set_index('date', inplace=True)
            obs_data['value'] = obs_data['value'].astype(float)
            st.write(obs_data)

        elif response.status_code != 200 and id and start and end:
            st.write('Failed to retrieve data. Status code:', response.status_code)
    
    
    