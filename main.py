# IMPORTS
import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import requests

# IMPORT OTHER FILES
from FRED.fred import load_fred
from EIA.eia import load_eia
from home import load_home


load_dotenv()
# FRED API SETUP
FRED_API_KEY = os.getenv("FRED_API")
base_url = "https://api.stlouisfed.org/fred/"

# EIA API SETUP


# SETUP
with st.sidebar:
    st.header("Natural Gas Dashboard")

current_page = st.sidebar.radio(
    'Data Source', 
    ['Home', 'FRED', 'EIA']
)
if current_page == 'Home':
    load_home()
elif current_page == 'FRED':
    load_fred()
elif current_page == 'EIA':
    load_eia()