import pytest
import random
import string
from utils.test_payloads import valid_add_pet_payload, invalid_add_pet_payloads

@pytest.mark.parametrize("status, expected_status_code", [
    ("available", 200),
    ("pending", 200),
    ("sold", 200),
    ("invalid", 400),
    ("A1", 400),
    (-1, 400),
    (9999999999999999999999, 400)
])
def test_get_pets_by_status(api_client, status, expected_status_code):
    response = api_client.get("/pet/findByStatus", params={"status": status})

    # Assert the response status code
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, got {response.status_code} for pet status: {status}"
    )
    if expected_status_code == 200:
        response_data = response.json()
        assert isinstance(response_data, list), "Response should be a list of pets"

@pytest.mark.parametrize("pet_id, expected_status_code", [
    ("valid", 200),         # Placeholder for a valid pet ID, fetched from the fixture
    (None, 404),            # Explicitly testing None as an invalid pet ID
    ("invalid_id", 400),    # String instead of an integer
    (-1, 400),              # Negative number as invalid ID
    (999999999, 404),    # Non-existent valid format ID
])
def test_get_pet_by_id(api_client, get_pet_ids_by_status, pet_id, expected_status_code):
    if pet_id == "valid":
        # Fetch a valid pet ID for this test
        pet_ids = get_pet_ids_by_status("available")
        assert pet_ids, "No pet IDs found for status 'available'"
        pet_id = pet_ids[0]

    # Make the API call
    response = api_client.get(f"/pet/{pet_id}")

    # Assert the response status code
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, got {response.status_code} for pet_id: {pet_id}"
    )

@pytest.mark.parametrize("with_image, expected_status_code", [
    (True, 200),  # With image, expect 200 status code
    (False, 400), # Without image, expect 400 status code (assuming the API expects an image)
])
def test_post_upload_image_to_pet(api_client, sample_image_path, get_pet_ids_by_status,with_image,expected_status_code): 
    pet_ids = get_pet_ids_by_status("available")
    assert pet_ids, "No pet IDs found for status 'available'"
    pet_id = pet_ids[0]
    if with_image:
        with open(sample_image_path, "rb") as image_file:
            response = api_client.post(f"/pet/{pet_id}/uploadImage", data=None, headers=None, files={"file": image_file})
            assert response.status_code == expected_status_code,(
             f"Expected status code {expected_status_code}, got {response.status_code} for pet_id: {pet_id}"
            )
    else:
        response = api_client.post(f"/pet/{pet_id}/uploadImage", data=None, headers=None, files=None)
        assert response.status_code == expected_status_code,(
             f"Expected status code {expected_status_code}, got {response.status_code} for pet_id: {pet_id}"
            )
        
@pytest.mark.parametrize("payload, expected_status_code", [
    (valid_add_pet_payload, 200),  # Valid input
    *(zip(invalid_add_pet_payloads, [405] * len(invalid_add_pet_payloads)))  # Invalid inputs
])
def test_add_pet(api_client, payload, expected_status_code):
    """
    Test to add a pet to the store using the /pet endpoint with both valid and invalid inputs.
    """
    response = api_client.post("/pet", data=payload, headers={"Content-Type": "application/json"})

    # Assert the status code
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, got {response.status_code} for payload: {payload}"
    )

    if response.status_code == 200:
        # For valid input, validate the response body
        response_data = response.json()
        assert response_data["id"] > 0, "Expected a positive ID for the newly created pet"
        assert response_data["name"] == payload["name"], "Pet name in response does not match"
        assert response_data["status"] == payload["status"], "Pet status in response does not match"
        assert "category" in response_data, "Category information is missing in response"
        assert "photoUrls" in response_data, "Photo URLs are missing in response"
    elif response.status_code == 405:
        # For invalid input, check for an appropriate error message
        error_message = response.json().get("message", "")
        assert "Invalid input" in error_message, (
            f"Expected error message containing 'Invalid input', got: {error_message}"
        )

@pytest.mark.parametrize("pet_id, updated_name, updated_status, expected_status_code", [
    # Valid inputs with a valid pet ID
    (None, "Kitty", "available", 200),   

    # Valid inputs with an invalid pet ID
    (-1, "Kitty", "available", 404),    # Invalid pet ID
    (999999999, "Buddy", "pending", 404), # Non-existent pet ID

    # Valid inputs without a pet ID
    (None, "Kitty", "available", 405),  # Missing pet ID
])
def test_update_pet_with_form_data(api_client, get_pet_ids_by_status, pet_id, updated_name, updated_status, expected_status_code):
    # Step 1: Handle valid pet ID retrieval only if pet_id is None for valid cases
    if pet_id is None and expected_status_code == 200:
        pet_ids = get_pet_ids_by_status("sold")
        assert pet_ids, "No pet IDs found for status 'sold'"
        pet_id = pet_ids[0]  # Use the first valid pet ID

    # Step 2: Construct the API endpoint
    endpoint = f"/pet/{pet_id}" if pet_id is not None else "/pet"

    # Step 3: Send the update request using form data
    form_data = {
        "name": updated_name,
        "status": updated_status,
    }
    response = api_client.post(endpoint, data=form_data, headers={"Content-Type": "application/x-www-form-urlencoded"})
    
    # Step 4: Validate the response status code
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, got {response.status_code}. "
        f"Form Data: {form_data}, Endpoint: {endpoint}, Response: {response.text}"
    )

    # Step 5: If the update was successful, verify using GET
    if response.status_code == 200:
        get_response = api_client.get(f"/pet/{pet_id}")
        assert get_response.status_code == 200, (
            f"Failed to fetch pet after update: {get_response.status_code}, {get_response.text}"
        )

        # Validate the updated fields
        try:
            pet_data = get_response.json()
            assert pet_data["name"] == updated_name, (
                f"Expected name: {updated_name}, got: {pet_data['name']} for pet_id: {pet_id}"
            )
            assert pet_data["status"] == updated_status, (
                f"Expected status: {updated_status}, got: {pet_data['status']} for pet_id: {pet_id}"
            )
        except KeyError as e:
            pytest.fail(f"Field '{e.args[0]}' not found for pet_id: {pet_id}.")
            
@pytest.mark.parametrize("pet_id, updated_name, updated_status, expected_status_code", [
    # Valid inputs with a valid pet ID
    (None, "Random Name", "available", 200),  

    # Valid inputs with a invalid pet ID
    (999999, "Random Name", "available", 404), 
    # Invalid pet ID
    (0, "Buddy", "available", 400),  # Non-existent pet ID
    
    # Empty JSON Body
    (None, None, None, 405),  # Empty body (invalid request)
])
def test_update_pet_with_put(api_client, get_pet_ids_by_status, pet_id, updated_name, updated_status, expected_status_code):
    # Step 1: Fetch an existing pet if pet_id is None
    if pet_id is None:
        pet_ids = get_pet_ids_by_status("available")
        assert pet_ids, "No pet IDs found for status 'available'"
        pet_id = pet_ids[0]  # Use the first available pet ID
    if expected_status_code==200:
        updated_name = updated_name + ''.join(random.choices(string.ascii_lowercase, k=5))
    
    
    # Step 2: Create the JSON payload for the update
    if updated_name is None and updated_status is None:
        json_payload={}
    else:
        json_payload = {
            "id": pet_id,
            "category": {"id": 0, "name": "string"},
            "name": updated_name if updated_name else "default_name",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": updated_status if updated_status else "available"
        }
    
    # Step 3: Send the PUT request to update the pet
    response = api_client.put("/pet", json=json_payload, headers={"Content-Type": "application/json"})
    
    # Step 4: Assert the response code
    assert response.status_code == expected_status_code, f"Update call failed for pet_id : {pet_id}. Expected response status : {expected_status_code} and received response : {response.status_code}, {response.text}"
    
    # Step 5: If the response code is 200, fetch the pet again and verify
    if response.status_code == 200:
        get_response = api_client.get(f"/pet/{pet_id}")
        assert get_response.status_code == 200, f"Failed to fetch pet after update: {get_response.status_code}, {get_response.text}"

        # Step 6: Verify the updated name and status
        try:
            pet_data = get_response.json()
            assert pet_data["id"] == pet_id, f"Expected pet_id: {pet_id}, got: {pet_data['id']}"
            assert pet_data["name"] == updated_name, f"Expected name: {updated_name}, got: {pet_data['name']} for pet_id: {pet_id}"
            assert pet_data["status"] == updated_status, f"Expected status: {updated_status}, got: {pet_data['status']} for pet_id: {pet_id}"
        except KeyError as e:
            pytest.fail(f"Field {str(e)} not found in response for pet_id: {pet_id}")
            
@pytest.mark.parametrize("pet_id, api_key, expected_status_code", [
    # Valid pet id and valid key
    (None, "special-key", 200),

    # Valid pet id and invalid key
    (None, "invalid-key", 403),

    # Invalid pet id and valid key
    (0, "special-key", 404),
    (-1, "special-key", 400),

    # Invalid pet id and invalid key
    (0, "invalid-key", 403),
])
def test_delete_pet(api_client, pet_id, api_key, expected_status_code):
    # Step 1: Create the pet if pet_id is None
    if pet_id is None:
        pet_name = "Doggie" + ''.join(random.choices(string.ascii_lowercase, k=5))  # Generate a unique name
        pet_status = "available"

        # Use the valid_add_pet_payload and update name dynamically
        json_payload = valid_add_pet_payload.copy()
        json_payload["name"] = pet_name
        json_payload["status"] = pet_status
        
        # Define headers for the POST call
        post_headers = {
            "Content-Type": "application/json"
        }

        # Create the pet using the POST API call
        create_response = api_client.post("/pet", data=json_payload, headers=post_headers)
        
        # Assert that the pet was created successfully
        assert create_response.status_code == 200, f"Failed to create pet: {create_response.status_code}, {create_response.text}"
        
        # Get the pet_id from the response
        pet_id = create_response.json().get("id")
        assert pet_id, "Failed to retrieve pet_id from the create response"
    
    # Step 2: Define headers for the DELETE call with api_key
    delete_headers = {
        "api_key": api_key  # Use the parameterized API key
    }

    # Step 3: Delete the pet using the DELETE API call
    delete_response = api_client.delete(f"/pet/{pet_id}", headers=delete_headers)
    
    # Assert that the response status matches the expected value
    assert delete_response.status_code == expected_status_code, f"Delete call failed for pet_id : {pet_id}. Expected response status : {expected_status_code} and received response : {delete_response.status_code}, {delete_response.text}"
    
    # Step 4: If the pet was deleted successfully (status 200), verify it no longer exists
    if delete_response.status_code == 200:
        get_response = api_client.get(f"/pet/{pet_id}")
        
        # Assert that the GET request returns a 404 status code and the message "Pet not found"
        assert get_response.status_code == 404, f"Expected status code 404, got: {get_response.status_code}"
        assert get_response.json().get("message") == "Pet not found", f"Expected message 'Pet not found', got: {get_response.json().get('message')}"