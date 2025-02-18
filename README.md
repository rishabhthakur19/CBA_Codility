# Pet Store API Tests

This repository contains automated API tests for the Pet API collection from the Pet Store application using Python and Playwright. Below are the steps required to set up and execute these tests on a new system.

## Prerequisites

1. Install Python (>= 3.7) from [Python.org](https://www.python.org/).
2. Ensure `pip` (Python package manager) is installed. It typically comes with Python.
3. Install Playwright:
   ```bash
   pip install playwright
   playwright install
   ```
4. Install Allure for generating test reports. Use the following command to install it globally:
   ```bash
   npm install -g allure-commandline --save-dev
   ```
5. Install pytest-xdist for enabling parallel test execution:
   ```bash
   pip install pytest-xdist
   ```
6. Install urllib3 to supress InsecureRequestWarning
   ```bash
   pip install urllib3
   ```

## Directory Structure

```
PetStoreAPITests/
├── tests/
│   ├── test files
├── utils/
    ├── api_client.py
    ├── config.py
    ├── test_payloads.py
├── conftest.py
├── pytest.ini
```

## Installation (I have used visual studio code as my editor)

1. Navigate to the root directory of the project.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
## Discovering tests in the test explorer 
To ensure that the tests are discoverable in the test explorer do the following:
1. Ensure pytest is recognized in visual studio code 
   - Open the Command Palette in VS Code: Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS).
   - Type Python: Select Interpreter and press Enter.
   - Select the interpreter where pytest is installed. 
   - If you're using a virtual environment, select the virtual environment's Python interpreter.

2. Ensure test framework is configured in VS Code 
   - Open Settings: Press Ctrl + , or go to File > Preferences > Settings.
   - Search for python.testing in the search bar.
   - Ensure these settings are correctly configured:
      - python.testing.pytestEnabled: Set to true.
      - python.testing.autoTestDiscoverOnSave: Set to true (this will trigger test  discovery whenever you save your test files).

## Running Tests

### Sequential Test Runs
To run the tests sequentially and generate Allure results:
```bash
python -m pytest -n auto --alluredir=allure-results
```

### Parallel Test Runs
To run the tests in parallel and generate Allure results:
```bash
python -m pytest -n auto --alluredir=allure-results
```

## Generating Allure Reports
After running the tests, generate the Allure report with:
```bash
allure generate --single-file allure-results --clean
```

This will create an `allure-report` directory with the report.

## Notes
- Ensure all dependencies are installed correctly as outlined above.
- Modify `config.py` in the `utils` directory to include your test-specific configurations.
- The tests are designed to work with the Sauce Labs application. Update the test files as needed for other applications or environments.

