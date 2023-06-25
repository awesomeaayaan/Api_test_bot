# from qrlib.QRComponent import QRComponent
import requests

class APIComponent:
    def __init__(self):
        super().__init__()
        self.url = 'http://127.0.0.1:5000/items'

    def get_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
            data = response.json()
            # print(data)
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


bot = APIComponent()
bot.get_data()
