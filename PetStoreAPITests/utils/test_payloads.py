# Valid payload for adding a pet
valid_add_pet_payload = {
    "id": 0,
    "category": {"id": 1, "name": "Dogs"},
    "name": "Doggie",
    "photoUrls": ["https://example.com/dog.jpg"],
    "tags": [{"id": 1, "name": "Puppy"}],
    "status": "available"
}

# Invalid payloads for pet API calls
invalid_add_pet_payloads = [
    {
        # Missing required fields
        "category": {"name": "Dogs"},
        "photoUrls": [],
    },
    {
        # Incorrect data types
        "id": "invalid_id",  # ID should be an integer
        "category": {"id": "invalid", "name": 123},  # Invalid types
        "name": 1234,  # Name should be a string
        "photoUrls": "invalid_url",  # Should be a list
        "tags": "invalid_tags",  # Should be a list
        "status": "unknown"  # Status not in allowed values
    },
    {
        #Empty payload
    }
]