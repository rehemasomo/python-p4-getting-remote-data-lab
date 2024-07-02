import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  

    def load_json(self):
        response_content = self.get_response_body()
        return json.loads(response_content.decode('utf-8'))  
