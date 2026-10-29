HIDR Website Testing Project
Project Overview
This project focuses on testing the HIDR website using both manual testing and automation.

Selected test scenarios are automated using Python, Selenium WebDriver and pytest. Other pages and scenarios are tested manually where manual verification is more suitable.

Website: https://hidr.com.np/
Tools & Technologies
- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)
- Google Chrome
- Git & GitHub
Project Structure
HIDR_Automation_Test/
│
├── pages/              # Page and component classes
├── tests/              # Automated test cases
├── screenshots/        # Test screenshots
├── reports/            # Test reports
├── test_data/          # Test data
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md


Testing Approach
- Manual Testing: Used for exploratory testing, visual checks and scenarios requiring human observation.
- Automation Testing: Used for stable and repeatable scenarios with clear expected results.
- Positive Testing: Checks valid inputs and expected behavior.
- Negative Testing: Checks invalid inputs and error handling.
- Functional Testing: Checks page elements, links, buttons and navigation.
Automation Coverage
Automation has been implemented for selected areas:
- Home page
- Header and Footer components
- Blog page
- Books page
- Career page
- Contact page
- Reports page
Not every HIDR page is automated. Some pages and scenarios are covered through manual testing where appropriate.
Setup
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL


2. Open the project folder
cd HIDR_Automation_Test


3. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1


4. Install dependencies
python -m pip install -r requirements.txt


Run Tests
Run all tests:
python -m pytest -v


Run a specific test file:
python -m pytest tests/test_contact_page.py -v


Generate an HTML report:
python -m pytest --html=reports/report.html --self-contained-html


Project Status
Status: Ongoing

Automation coverage will be expanded as suitable test scenarios are identified.
Author
Chandan Sah
BSc (Hons) Information Technology
Aspiring QA Engineer | Manual & Automation Testing