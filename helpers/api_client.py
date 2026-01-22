import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, endpoint):
        """GET request helper"""
        url = f"{self.base_url}{endpoint}"
        return requests.get(url)
    
    def post(self, endpoint, data):
        """POST request helper"""
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=data)
    
    def put(self, endpoint, data):
        """PUT request helper"""
        url = f"{self.base_url}{endpoint}"
        return requests.put(url, json=data)
    
    def delete(self, endpoint):
        """DELETE request helper"""
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url)