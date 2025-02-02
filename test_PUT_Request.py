import requests
import pytest

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define the endpoint
ENDPOINT = '/posts/1'

#Provide the Payload
PAYLOAD = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
}

def send_put_request(base_url, endpoint,payload):
    url = f"{base_url}{endpoint}"
    response = requests.put(url,payload)
    return response

def test_put_request_status_code():
    """
    Test the PUT request to the /users endpoint to ensure it returns a 200 status code.
    """
    response = send_put_request(BASE_URL, ENDPOINT,PAYLOAD)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

# If running the script directly, it will execute the tests
if __name__ == "__main__":
    pytest.main()
