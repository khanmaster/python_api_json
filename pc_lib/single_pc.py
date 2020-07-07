from .config_manager import base_url
from .models.single_postcode_model import SinglePCModel
import requests


class SinglePC():

    def __init__(self, single_postcode):
        self.url = base_url() + f"postcodes/{single_postcode}"
        self.request = requests.get(self.url)
        self.header_details = self.request.headers
        self.response_json = self.request.json()

    def response(self):
        return SinglePCModel(self.response_json)