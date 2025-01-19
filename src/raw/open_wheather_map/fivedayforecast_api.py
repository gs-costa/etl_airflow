from datetime import datetime
import json
from typing import Dict
import requests
from raw.open_wheather_map.geocoding_api import GeoCoding
from common.environment import Env


class FiveDayForecast:

    def __init__(self):
        self.endpoint = "/data/2.5/forecast"
        self.geocoding = GeoCoding()

    def __build_params(self) -> Dict:
        geocoding_response = self.geocoding.get()
        latitude = geocoding_response[0].get("lat")
        longitude = geocoding_response[0].get("lon")
        return {"lat": latitude, "lon": longitude, "appid": Env.OPENWHEATERMAP_APPID}

    def get(self) -> Dict:
        endpoint_url = f"{Env.OPENWHEATERMAP_BASE_URL}{self.endpoint}"
        params = self.__build_params()
        response = requests.get(url=endpoint_url, params=params)
        return response.json()

    def save_file(self, data: Dict, file_path: str):
        with open(file_path, "w") as file:
            file.write(json.dumps(data))

    def execute(self):
        execution_date = datetime.today()
        data = self.get()
        self.save_file(data=data, file_path=f"./raw_data/{execution_date}.json")


if __name__ == "__main__":
    FiveDayForecast().execute()
