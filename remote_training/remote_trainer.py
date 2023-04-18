import requests

class RemoteTrainer:
    proxies = {
        "http": "http://127.0.0.1:1080",
        "https": "http://127.0.0.1:1080"
    }
    def __init__(self, server_url):
        self.server_url = server_url

    def start_training(self, config,proxies=proxies):
        response = requests.post(f"{self.server_url}/train", json=config,proxies=proxies)
        response.raise_for_status()
        return response.json()
