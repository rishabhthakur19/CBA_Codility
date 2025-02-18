# Test Strategy

## Objective:
Ensure the Pet Collection APIs of the Pet Store Application are functional

## Scope:
1. **Functional Testing**:
   - **Pet Collection API**:
     - Add Pet
     - Get Pet by ID
     - Update Pet
     - Delete Pet

2. **Regression Testing**:
   - Ensure API stability after updates or modifications to the application.

3. **Error Handling**:
   - Ensure that the APIs return appropriate error codes (400, 404, etc.) for invalid input or non-existing resources.

## Test Types:
1. **Functional**: 
   - Verify the core API functionalities work as expected for each collection (Pet, Store, User).
2. **Regression**: 
   - Ensure that new changes do not break existing functionality.
3. **Error Handling**: 
   - Verify that error responses are returned for invalid inputs, missing fields, and other erroneous cases.
4. **Boundary Testing**: 
   - Test edge cases such as empty payloads, malformed data, and large input sizes.

## Key Tools:
- **Python + Pytest**: For API automation testing.
- **Allure**: For generating detailed and interactive reports.

## Reporting and Monitoring:
- **Allure Report**: For detailed, interactive test reports with test execution timelines and error details.

## Bug Reporting Guidelines:
**Severity and Priority**:
- **Critical**: Blocks core API functionality (e.g., user login fails, pet creation fails).
- **High**: Major workflow issues (e.g., incorrect responses from the store API, inability to retrieve user details).
- **Medium**: Partial functionality issues (e.g., incorrect status on a pet or order, mismatched data fields).
- **Low**: Minor issues or cosmetic errors (e.g., non-impactful response code discrepancies).

## Test Environment:
- **Base URL**: The environment’s base URL needs to be specified in the `config.py` file.
- **Test Data**: Sample data for creating users can be found in the `test_payloads.py` file within the `utils` folder.

---

# Test Plan for Pet Collection API

## Objective
This test plan validates the functionality of the Pet Management API, specifically focusing on the creation, retrieval, update, and deletion of pet records. The tests cover various scenarios including valid and invalid pet IDs, correct and incorrect API keys, and correct handling of request payloads.

## Test Scenarios

### 1. **Create Pet**

#### Objective:
Ensure that a pet can be successfully created with a valid payload.

#### Test Steps:
1. Make a POST request to the `/pet` endpoint with a valid payload.
2. Validate the response status code is `200 OK`.
3. Verify the pet is created successfully by checking if the `id` is returned in the response.

#### Test Data:
- **Valid Payload:**
    - Name: `Doggie`
    - Status: `available`
    - Category: `Dogs`
    - Tags: `Puppy`
    - PhotoUrls: `https://example.com/dog.jpg`

#### Expected Result:
- A valid pet ID is returned.
- Status code: `200 OK`.

---

### 2. **Update Pet**

#### Objective:
Validate the pet update functionality using the `/pet` endpoint with the provided `pet_id`.

#### Test Steps:
1. If `pet_id` is `None`, create a new pet using the valid payload.
2. Send a PUT request to update the pet details using the `/pet` endpoint.
3. Validate that the status code is `200 OK`.
4. Retrieve the pet and validate that the updated `name` and `status` are correct.

#### Test Data (Parameterization):
- **Valid pet ID and valid key**:
    - `pet_id`: Generated or provided pet ID
    - `updated_name`: Dynamically generated unique name (e.g., `Kitty`)
    - `updated_status`: Status to update, e.g., `available`
    - API key: `special-key`

- **Valid pet ID and invalid key**:
    - `pet_id`: Valid pet ID
    - API key: `invalid-key`

- **Invalid pet ID and valid key**:
    - `pet_id`: Invalid pet ID (e.g., `999999`)
    - API key: `special-key`

- **Invalid pet ID and invalid key**:
    - `pet_id`: Invalid pet ID
    - API key: `invalid-key`

#### Expected Result:
- If valid pet ID is provided, pet data should be updated successfully.
- If invalid pet ID or incorrect API key is provided, appropriate error responses should be returned (e.g., `404 Not Found`, `403 Forbidden`).

---

### 3. **Delete Pet**

#### Objective:
Ensure that a pet can be successfully deleted using the `/pet/{pet_id}` endpoint, and the deleted pet cannot be found.

#### Test Steps:
1. If `pet_id` is `None`, create a new pet using the valid payload.
2. Send a DELETE request to `/pet/{pet_id}`.
3. Validate that the status code is `200 OK`.
4. Try to retrieve the deleted pet using a GET request and validate that the status code is `404 Not Found` and the response message is `Pet not found`.

#### Test Data (Parameterization):
- **Valid pet ID and valid key**:
    - `pet_id`: Generated or provided pet ID
    - API key: `special-key`

- **Valid pet ID and invalid key**:
    - `pet_id`: Valid pet ID
    - API key: `invalid-key`

- **Invalid pet ID and valid key**:
    - `pet_id`: Invalid pet ID (e.g., `999999`)
    - API key: `special-key`

- **Invalid pet ID and invalid key**:
    - `pet_id`: Invalid pet ID
    - API key: `invalid-key`

#### Expected Result:
- If valid pet ID and key are provided, the pet should be deleted successfully.
- If invalid pet ID or incorrect API key is provided, appropriate error responses should be returned (`404 Not Found` for invalid pet ID, `403 Forbidden` for invalid key).
- After deletion, attempting to fetch the pet should return `404 Not Found` with the message `Pet not found`.

---

## Test Environment
- **API Base URL**: `https://petstore.swagger.io/v2`
- **Test Tools**: Pytest, requests
- **Testing Framework**: Pytest
- **Test Data**: Valid and invalid pet data

## Test Coverage

- **API Methods**:
    - `POST /pet`: Create pet
    - `PUT /pet`: Update pet
    - `DELETE /pet/{pet_id}`: Delete pet
    - `GET /pet/{pet_id}`: Retrieve pet by ID

- **Test Cases**:
    - **Create Pet**: Valid pet creation.
    - **Update Pet**: Updating a pet's name and status.
    - **Delete Pet**: Deleting a pet and confirming deletion.

## Test Result Reporting
- The results of the tests will be reported in the console with the status for each test case.
- **Success Criteria**: The tests will pass if the status codes and response messages match the expected values.

## Test Dependencies
- **API Key**: Some of the test cases require valid and invalid API keys to verify authentication.
- **Pet ID**: For update and delete operations, valid and invalid pet IDs will be used.

## Conclusion
This test plan ensures that the Pet Management API behaves as expected under various scenarios including valid and invalid inputs, proper error handling, and correct API key usage.

---

# Framework Selection

## Framework: Python + Playwright

### Reasons for Selection:
- **Modern & Efficient**: Handles dynamic web applications better than Selenium.
- **Ease of Use**: Offers a clean API with automatic waiting.
- **Cross-Browser Testing**: Supports Chromium, Firefox, and WebKit with a unified API.
- **Built-in Features**: Includes tracing, screenshot capture, and video recording for enhanced debugging.
- **Seamless CI Integration**: Lightweight and integrates smoothly with continuous integration systems like GitHub Actions.

---
