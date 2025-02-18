import pytest
from utils.api_client import APIClient
from utils.config import BASE_URL

@pytest.fixture(scope="session")
def api_client():
    return APIClient(BASE_URL)

@pytest.fixture(scope="function")
def get_pet_ids_by_status(api_client):
    """
    Fetch pet IDs by status using the API client.
    """
    def fetch_ids(status):
        response = api_client.get("/pet/findByStatus", params={"status": status})
        assert response.status_code == 200, f"Failed to fetch pets with status {status}"
        return [pet["id"] for pet in response.json() if "id" in pet]
    return fetch_ids
