import requests

class RemoteTrainer:
    def __init__(self, server_url):
        self.server_url = server_url

    def start_training(self, config):
        response = requests.post(f"{self.server_url}/train", json=config)
        return response.json()
