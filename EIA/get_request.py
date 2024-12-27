import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
EIA_API_KEY = os.getenv("EIA_API")


# [ [NAME, URL, FREQUENCY] ]

url_database = [
    ['Number of Producing Gas Wells',  'https://api.eia.gov/v2/natural-gas/prod/wells/data/?', 'annual'],
    ['Gross Withdrawals and Production', 'https://api.eia.gov/v2/natural-gas/prod/sum/data/?', 'monthly'],
    ['Natural Gas Plant Processing', 'https://api.eia.gov/v2/natural-gas/prod/pp/data/?', 'monthly'],
    ['Natural Gas Plant Liquids Production', 'https://api.eia.gov/v2/natural-gas/prod/ngpl/data/?', 'annual'],
    ['Offshore Gross Withdrawals of Natural Gas', 'https://api.eia.gov/v2/natural-gas/prod/off/data/?', 'monthly'],
    ['Weekly Working Gas in Underground Storage', 'https://api.eia.gov/v2/natural-gas/stor/wkly/data/?', 'weekly'],
    ['Underground Natural Gas Storage By All Operators', 'https://api.eia.gov/v2/natural-gas/stor/sum/data/?', 'monthly'],
    ['U.S Underground Natural Gas Storage By Storage Type', 'https://api.eia.gov/v2/natural-gas/stor/type/data/?', 'monthly'],
    ['Underground Natural Gas Storage Capacity', 'https://api.eia.gov/v2/natural-gas/stor/cap/data/?', 'monthly'],
    ['Liquefied Natural Gas Additions to and Withdrawals from Storage', 'https://api.eia.gov/v2/natural-gas/stor/lng/data/?', 'annual'],
    ['Number of Natural Gas Consumers', 'https://api.eia.gov/v2/natural-gas/cons/num/data/?', 'annual'],
    ['Natural Gas Consumers By End Use', 'https://api.eia.gov/v2/natural-gas/cons/sum/data/?', 'monthly'],
    ['U.S. Natural Gas Imports & Exports by State', 'https://api.eia.gov/v2/natural-gas/move/state/data/?', 'monthly'],
    ['U.S Natural Gas Imports By Country', 'https://api.eia.gov/v2/natural-gas/move/impc/data/?', 'monthly'],
    ['U.S Natural Gas Exports and Re-exports By Country', 'https://api.eia.gov/v2/natural-gas/move/expc/data/?', 'monthly']
]


def reload_data(url_database):
    for item in url_database:
        get_eia_data(item[0], item[1], item[2])
    clean_data()
        
def clean_data():
    pass

def get_eia_data(name, url, freq):
    req = requests.get(url + "api_key=" + EIA_API_KEY, 
                            params={"frequency": f"{freq}", "data[0]": "value", "sort[0][column]": "period", 
                                    "sort[0][direction]": "desc", "offset": 0, "length": 5000})
    data = req.json()
    df = pd.DataFrame(data.get("response", {}).get("data", []))
    df.to_csv(f"EIA/{name}.csv", index=False)
    
reload_data(url_database)