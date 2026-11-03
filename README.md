# Flask Getting Remote Data Lab

## Project Overview

This project implements a reusable Python class called `GetRequester` for retrieving data from remote APIs using HTTP GET requests.

The class accepts a URL during initialization, retrieves the raw HTTP response, and provides a method for converting JSON responses into native Python data structures.

The project uses a company directory API as an example, retrieving employee information such as names and occupations.

## Features

- Reusable `GetRequester` class.
- HTTP GET requests using the Python `requests` library.
- Retrieves raw response content as bytes.
- Converts JSON responses into Python lists and dictionaries.
- HTTP error handling using `raise_for_status()`.
- Request timeout of 10 seconds.
- Automated tests using pytest.

## Technologies Used

- Python 3
- Requests
- JSON
- Pytest
- Git and GitHub

## API Endpoint

The project uses the following remote JSON endpoint:

https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json

## Project Structure

```text
flask-getting-remote-data-lab/
│
├── lib/
│   ├── GetRequester.py
│   └── testing/
│       ├── conftest.py
│       └── get_requester_test.py
│
├── Pipfile
├── Pipfile.lock
├── pytest.ini
├── README.md
├── .gitignore
└── LICENSE.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/petermulwa33/flask-getting-remote-data-lab.git

cd flask-getting-remote-data-lab
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Activate the virtual environment

```bash
pipenv shell
```

## Implementation

The `GetRequester` class is implemented in `lib/GetRequester.py`.

### get_response_body()

This method sends an HTTP GET request to the URL provided during initialization.

It returns the raw response body as bytes and raises an exception when the HTTP request returns an unsuccessful status code.

### load_json()

This method calls `get_response_body()` and uses Python's built-in JSON module to convert the response into native Python data structures.

## Usage Example

```python
from GetRequester import GetRequester

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

requester = GetRequester(url)

# Retrieve raw response
response = requester.get_response_body()
print(response)

# Convert JSON into Python objects
employees = requester.load_json()
print(employees)

# Check the resulting data type
print(type(employees))
```

The parsed response is a Python list containing dictionaries representing employees.

Example:

```python
[
    {
        "name": "Daniel",
        "occupation": "LG Fridge Salesman"
    },
    {
        "name": "Joe",
        "occupation": "WiFi Fixer"
    }
]
```

## Running Tests

Run the automated test suite from the project root:

```bash
pytest -v
```

The test suite verifies:

1. `get_response_body()` returns the expected raw response.
2. `load_json()` correctly converts the JSON response into Python data.

### Test Results

**Latest test result: 2 passed, 0 failed.**

The test suite reports some deprecation warnings originating from the installed pytest assertion-rewriting implementation.

## Tools and Resources

- [GitHub Curriculum Repository](https://github.com/learn-co-curriculum/flask-getting-remote-data-lab)
- [Mozilla Developer Network - HTTP GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
- [Mozilla Developer Network - HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Make a README](https://makeareadme.com/)

## Learning Objectives

This lab demonstrates:

- Object-oriented programming in Python.
- Making HTTP requests to external APIs.
- Retrieving remote data.
- Working with JSON responses.
- Converting JSON into Python data structures.
- Writing and running automated tests.
- Using Git branches and GitHub pull requests.

## Submission

Once all tests pass and the completed implementation has been merged into the GitHub `main` branch, submit the repository through Canvas using CodeGrade.