import requests
import pytest

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define the endpoint
ENDPOINT = '/posts/1'  # Deleting post with ID 1

def send_delete_request(base_url, endpoint):
    url = f"{base_url}{endpoint}"
    response = requests.delete(url)
    return response

def test_delete_request_status_code():
    response = send_delete_request(BASE_URL, ENDPOINT)
    assert response.status_code in [200, 204], f"Expected status code 200 or 204 but got {response.status_code}"

# If running the script directly, it will execute the tests
if __name__ == "__main__":
    pytest.main()
