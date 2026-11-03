
import requests
import json


class GetRequester:

    def __init__(self, url):
        # Store the API URL
        self.url = url

    def get_response_body(self):
        # Send GET request with a 10-second timeout
        response = requests.get(self.url, timeout=10)

        # Raise an exception for unsuccessful HTTP responses
        response.raise_for_status()

        # Return raw response bytes
        return response.content

    def load_json(self):
        # Retrieve the response body
        response_body = self.get_response_body()

        # Convert JSON bytes into Python objects
        return json.loads(response_body)
