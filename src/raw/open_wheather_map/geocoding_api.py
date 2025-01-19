from typing import Dict, List
import requests
from common.environment import Env


class GeoCoding:

    def __init__(self):
        self.params = {
            "q": "Uberlandia,MG,Brazil",
            "appid": Env.OPENWHEATERMAP_APPID,
            "limit": 1,
        }
        self.endpoint = "/geo/1.0/direct"

    def get(self) -> List[Dict]:
        endpoint_url = f"{Env.OPENWHEATERMAP_BASE_URL}{self.endpoint}"
        response = requests.get(url=endpoint_url, params=self.params)
        return response.json()
