import requests
import pandas as pd

class CensusAPIWrapper:
    BASE_URL = "https://api.census.gov/data/2023/acs/acs5"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_state_data(self, variables):
        """Fetch data at state level"""
        params = {
            "get": ",".join(variables + ["NAME"]),
            "for": "state:*",
            "key": self.api_key
        }
        return self._make_request(params)

    def get_zip_data(self, variables):
        """Fetch data at ZIP code level (ZCTA)"""
        params = {
            "get": ",".join(variables + ["NAME"]),
            "for": "zip code tabulation area:*",
            "key": self.api_key
        }
        return self._make_request(params)

    def _make_request(self, params):
        """Shared request handling logic"""
        response = requests.get(self.BASE_URL, params=params)
        
        if response.status_code != 200:
            raise Exception(f"API Request Failed: {response.status_code} - {response.text}")

        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])
        
        # Clean column names
        df = df.rename(columns={
            "zip code tabulation area": "zip_code",
            "state": "state_fips"
        })
        
        return df