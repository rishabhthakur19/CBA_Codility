import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the specific InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _log_request_response(self, method, url, params=None, data=None, headers=None, response=None):
        """
        Logs the details of the request and the response.
        """
        print(f"\n--- {method.upper()} Request ---")
        print(f"URL: {url}")
        if params:
            print(f"Parameters: {params}")
        if data:
            print(f"Body: {data}")
        if headers:
            print(f"Headers: {headers}")
        print("\n--- Response ---")
        if response:
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=headers, verify=False)  # Disable SSL verification
        self._log_request_response("GET", url, params=params, headers=headers, response=response)
        return response

    def post(self, endpoint, data=None, headers=None, files=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=headers, files=files, verify=False)  # Disable SSL verification
        self._log_request_response("POST", url, data=data, headers=headers, response=response)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        
        # Use json if provided, otherwise fall back to data
        if json is not None:
            response = requests.put(url, json=json, headers=headers, verify=False)
            self._log_request_response("PUT", url, data=json, headers=headers, response=response)
        elif data is not None:
            response = requests.put(url, data=data, headers=headers, verify=False)
            self._log_request_response("PUT", url, data=data, headers=headers, response=response)
        else:
            # Handle the case where neither json nor data is provided
            response = requests.put(url, headers=headers, verify=False)
            self._log_request_response("PUT", url, headers=headers, response=response)
        
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers, verify=False)  # Disable SSL verification
        self._log_request_response("DELETE", url, headers=headers, response=response)
        return response
