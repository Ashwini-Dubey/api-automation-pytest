import requests
import pytest

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define the endpoint
ENDPOINT = '/users'

#Provide the Payload
PAYLOAD = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

def send_post_request(base_url, endpoint,payload):
    url = f"{base_url}{endpoint}"
    response = requests.post(url,payload)
    return response

def test_post_request_status_code():
    """
    Test the POST request to the /users endpoint to ensure it returns a 200 status code.
    """
    response = send_post_request(BASE_URL, ENDPOINT,PAYLOAD)
    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

# If running the script directly, it will execute the tests
if __name__ == "__main__":
    pytest.main()
