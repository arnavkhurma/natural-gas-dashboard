import streamlit as st
import os
import pandas as pd

data = pd.read_csv("EIA/natural_gas_data.csv")

# FRED PAGE
def load_eia():
    st.write("eia.py")
    st.write(data)