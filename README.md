# Learning Playwright with Python

This project is set up for learning web automation testing using Playwright with Python.

## Project Structure

```
Learning_Playwright/
├── tests/             # Test files directory
│   └── test_example.py # Sample test file
├── requirements.txt   # Project dependencies
└── README.md         # This file
```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Running Tests

To run the tests:
```bash
pytest tests/test_example.py
```

## Writing Tests

The `test_example.py` file contains a sample test that:
- Navigates to the Playwright website
- Checks the page title
- Clicks a link
- Verifies navigation

Use this as a template for creating your own tests.

## Next Steps

1. Study the example test in `tests/test_example.py`
2. Create new test files for different scenarios
3. Learn about Playwright's features like:
   - Page navigation
   - Element selection
   - Form interaction
   - Network monitoring
   - Screenshots and videos