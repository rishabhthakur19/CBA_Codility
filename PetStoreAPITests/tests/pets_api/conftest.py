import pytest
import os
from utils.api_client import APIClient
from utils.config import BASE_URL  # Import the base URL from your config file

@pytest.fixture(scope="module")
def api_client():
    """
    Provides an instance of APIClient initialized with the base URL.
    """
    return APIClient(BASE_URL)

@pytest.fixture(scope="module")
def sample_image_path():
    """
    Provides the path to the sample image used in tests.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
    return os.path.join(project_root, "sample_animal_image.jpg")