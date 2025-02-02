import requests
import pytest

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define the endpoint
ENDPOINT = '/users'

def send_get_request(base_url, endpoint):
    url = f"{base_url}{endpoint}"
    response = requests.get(url)
    return response

def test_get_request_status_code():
    """
    Test the GET request to the /users endpoint to ensure it returns a 200 status code.
    """
    response = send_get_request(BASE_URL, ENDPOINT)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

# If running the script directly, it will execute the tests
if __name__ == "__main__":
    pytest.main()
