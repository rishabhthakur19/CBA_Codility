# Bug Report Summary: Pet API Collection Issues

## Affected Module: Pet API Collection

### Overview
This report summarizes the issues observed in the Pet API Collection for various endpoints. These issues result in incorrect status codes being returned, as well as inconsistent behavior when interacting with the API.

---

## Bug Details

### 1. **Create Pet Entry with Invalid Payloads**

#### a. Empty JSON Payload
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When attempting to create a pet entry using an empty JSON payload, the API incorrectly returns a `200 OK` response instead of a `405 Method Not Allowed`.

- **Steps to Reproduce:**
  1. Send a POST request to `/pet` endpoint with an empty JSON payload.
  2. Observe that the response status is `200 OK` instead of `405 Method Not Allowed`.

- **Expected Behavior:**
  - The API should return a `405 Method Not Allowed` status when an empty JSON payload is sent.

- **Actual Behavior:**
  - The API returns a `200 OK` status, which is incorrect.

#### b. Incorrect JSON Payload
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When a POST request is sent with an incorrectly formatted JSON payload, the API incorrectly returns a `200 OK` response instead of a `405 Method Not Allowed`.

- **Steps to Reproduce:**
  1. Send a POST request to `/pet` endpoint with an incorrectly formatted JSON payload.
  2. Observe that the response status is `200 OK` instead of `405 Method Not Allowed`.

- **Expected Behavior:**
  - The API should return a `405 Method Not Allowed` status for incorrect JSON payloads.

- **Actual Behavior:**
  - The API returns a `200 OK` status, which is incorrect.

#### c. Invalid Values in JSON Payload
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When a POST request is sent with invalid values in the JSON payload, the API incorrectly returns a `500 Internal Server Error` instead of a `405 Method Not Allowed`.

- **Steps to Reproduce:**
  1. Send a POST request to `/pet` endpoint with invalid values in the JSON payload.
  2. Observe that the response status is `500 Internal Server Error` instead of `405 Method Not Allowed`.

- **Expected Behavior:**
  - The API should return a `405 Method Not Allowed` status when invalid values are provided in the JSON payload.

- **Actual Behavior:**
  - The API returns a `500 Internal Server Error`, which is incorrect.

---

### 2. **Delete Pet Endpoint with Invalid Pet ID**

#### a. Invalid Negative Pet ID
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When an invalid negative value for `pet_id` is provided in the DELETE request, the API incorrectly returns a `404 Not Found` response instead of a `400 Bad Request`.

- **Steps to Reproduce:**
  1. Send a DELETE request to `/pet/{pet_id}` with a negative pet ID (e.g., `pet_id = -1`).
  2. Observe that the response status is `404 Not Found` instead of `400 Bad Request`.

- **Expected Behavior:**
  - The API should return a `400 Bad Request` status for invalid negative pet IDs.

- **Actual Behavior:**
  - The API returns a `404 Not Found`, which is incorrect.

#### b. Invalid Positive Pet ID
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When an invalid positive pet ID is provided in the DELETE request, the API incorrectly returns a `404 Not Found` response instead of a `403 Forbidden`.

- **Steps to Reproduce:**
  1. Send a DELETE request to `/pet/{pet_id}` with an invalid positive pet ID (e.g., `pet_id = 999999`).
  2. Observe that the response status is `404 Not Found` instead of `403 Forbidden`.

- **Expected Behavior:**
  - The API should return a `403 Forbidden` status for an invalid positive pet ID.

- **Actual Behavior:**
  - The API returns a `404 Not Found`, which is incorrect.

#### c. No Pet ID and Valid JSON Body
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When no `pet_id` is provided in the DELETE request and a valid JSON body is sent, the API incorrectly returns a `200 OK` response instead of a `403 Forbidden`.

- **Steps to Reproduce:**
  1. Send a DELETE request to `/pet/` without providing a pet ID but with a valid JSON body.
  2. Observe that the response status is `200 OK` instead of `403 Forbidden`.

- **Expected Behavior:**
  - The API should return a `403 Forbidden` status when no `pet_id` is provided and a valid JSON body is sent.

- **Actual Behavior:**
  - The API returns a `200 OK`, which is incorrect.

---

### 3. **Get Pet by ID**

#### a. Invalid Negative Pet ID
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When an invalid negative pet ID is provided in the `GET` request, the API incorrectly returns a `404 Not Found` response instead of a `400 Bad Request`.

- **Steps to Reproduce:**
  1. Send a GET request to `/pet/{pet_id}` with a negative pet ID (e.g., `pet_id = -1`).
  2. Observe that the response status is `404 Not Found` instead of `400 Bad Request`.

- **Expected Behavior:**
  - The API should return a `400 Bad Request` status for invalid negative pet IDs.

- **Actual Behavior:**
  - The API returns a `404 Not Found`, which is incorrect.

#### b. Invalid Pet ID
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When an invalid pet ID is provided in the `GET` request (e.g., `pet_id = "abc"`), the API incorrectly returns a `404 Not Found` response instead of a `400 Bad Request`.

- **Steps to Reproduce:**
  1. Send a GET request to `/pet/{pet_id}` with an invalid pet ID (e.g., `pet_id = "abc"`).
  2. Observe that the response status is `404 Not Found` instead of `400 Bad Request`.

- **Expected Behavior:**
  - The API should return a `400 Bad Request` status for invalid pet IDs.

- **Actual Behavior:**
  - The API returns a `404 Not Found`, which is incorrect.

---

### 4. **Get Pet by Status**

#### a. Negative Value for Status Parameter
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When a negative value is provided for the `status` parameter, the API incorrectly returns a `200 OK` response instead of a `400 Bad Request`.

- **Steps to Reproduce:**
  1. Send a GET request to `/pet/findByStatus` with a negative value for the `status` parameter (e.g., `status = -1`).
  2. Observe that the response status is `200 OK` instead of `400 Bad Request`.

- **Expected Behavior:**
  - The API should return a `400 Bad Request` status for invalid status parameter values.

- **Actual Behavior:**
  - The API returns a `200 OK`, which is incorrect.

#### b. Invalid Status Parameter Value
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When an invalid status parameter value is provided (e.g., `status = "unknown"`,`status = 99999999999999999`, `status = -1`), the API incorrectly returns a `200 OK` response instead of a `400 Bad Request`.

- **Steps to Reproduce:**
  1. Send a GET request to `/pet/findByStatus` with an invalid value for the `status` parameter (e.g., `status = "unknown"`).
  2. Observe that the response status is `200 OK` instead of `400 Bad Request`.

- **Expected Behavior:**
  - The API should return a `400 Bad Request` status for invalid status parameter values.

- **Actual Behavior:**
  - The API returns a `200 OK`, which is incorrect.

---

### 5. **Upload Image to Pet**

#### a. No Image Attachment
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When attempting to upload an image to a pet without providing an image attachment, the API incorrectly returns a `415 Unsupported Media Type` response instead of a `400 Bad Request`.

- **Steps to Reproduce:**
  1. Send a POST request to `/pet/{pet_id}/uploadImage` without including an image attachment.
  2. Observe that the response status is `415 Unsupported Media Type` instead of `400 Bad Request`.

- **Expected Behavior:**
  - The API should return a `400 Bad Request` status when no image attachment is provided.

- **Actual Behavior:**
  - The API returns a `415 Unsupported Media Type`, which is incorrect.

---

### 6. **Update Pet with Form Data (POST Call)**

#### a. Details Not Updated
- **Severity:** High
- **Priority:** P2
- **Description:**
  - When using the POST method to update pet details with valid inputs, the update executes successfully with a `200 OK` response. However, when retrieving the pet data, the updated details are not reflected.

- **Steps to Reproduce:**
  1. Send a POST request to `/pet` with valid details to update a pet.
  2. After receiving the `200 OK` response, retrieve the pet and check if the updated details are present.
  3. Observe that the pet data has not been updated.

- **Expected Behavior:**
  - The pet details should be successfully updated, and the updated details should be retrievable.

- **Actual Behavior:**
  - The pet details are not updated even after receiving a `200 OK` response.

#### b. Valid inputs without a pet ID 
- **Severity:** High
- **Priority:** P2
- **Description:**
  - When using the POST method to update pet details with valid inputs without pet ID, the call gives `415 Unsupported Media` as response instead of `405 Invalid Input`

- **Steps to Reproduce:**
  1. Send a POST request to `/pet` with valid details without pet ID to update a pet.
  2. Observe that the response is `415 Unsupported Media` instead of `405 Invalid Input`

- **Expected Behavior:**
  - The call should give `405 Invalid Input` as a response

- **Actual Behavior:**
  - The call gives `415 Unsupported Media` as the response
---

### 7. **Update Pet with PUT Call**

#### a. Invalid Pet ID
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When updating a pet using the PUT method with an invalid `pet_id`, the API incorrectly returns a `200 OK` response instead of a `400 Bad Request`.

- **Steps to Reproduce:**
  1. Send a PUT request to `/pet` with an invalid pet ID (e.g., `pet_id = "abc"`).
  2. Observe that the response status is `200 OK` instead of `400 Bad Request`.

- **Expected Behavior:**
  - The API should return a `400 Bad Request` status for invalid pet IDs.

- **Actual Behavior:**
  - The API returns a `200 OK`, which is incorrect.

#### b. Empty JSON Body
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When updating a pet using the PUT method with an empty JSON body, the API incorrectly returns a `200 OK` response instead of a `405`.

- **Steps to Reproduce:**
  1. Send a PUT request to `/pet` with an empty JSON body.
  2. Observe that the response status is `200 OK` instead of `405`.

- **Expected Behavior:**
  - The API should return a `405` status for invalid pet IDs.

- **Actual Behavior:**
  - The API returns a `200 OK`, which is incorrect.

#### c. Non-Existing Pet ID
- **Severity:** High
- **Priority:** P1
- **Description:**
  - When updating a pet using the PUT method with an non existing Pet ID, the API incorrectly returns a `200 OK` response instead of a `404 Not Found` and also creates the a Pet having the provided Pet ID.

- **Steps to Reproduce:**
  1. Send a PUT request to `/pet` with a Non-Existing Pet ID.
  2. Observe that the response status is `200 OK` instead of `404 Not Found`.

- **Expected Behavior:**
  - The API should return a `404 Not Found` status for invalid pet IDs.

- **Actual Behavior:**
  - The API returns a `200 OK`, which is incorrect.
---

## Suggested Fixes
1. **General Response Codes**:
   - Ensure that the correct HTTP status codes are returned for each of the above scenarios.
2. **Validation Checks**:
   - Implement proper validation checks for empty payloads, invalid pet IDs, and missing required fields in requests.

---

## Additional Notes
- These issues significantly affect the reliability and functionality of the Pet API Collection. It is recommended to prioritize fixing them to ensure smooth API operations.

---

