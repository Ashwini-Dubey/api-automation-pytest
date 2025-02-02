# Pytest API Automation Framework

### **Overview**

This repository contains a pytest-based automation framework for API testing. The framework is designed to facilitate the testing of RESTful APIs with easy setup, flexible configuration, and detailed reporting.

### **Features**

* API Testing: Supports comprehensive testing of RESTful APIs.
* Data-Driven Testing: Easily handle multiple sets of test data.
* Detailed Reporting: Generate and view test reports with Allure or other reporting tools.
* Flexible Configuration: Use configuration files and environment variables for customization.
* Parallel Execution: Run tests concurrently to speed up the test suite.

### **Requirements**

* Python 3.x
* pytest
* requests (for making API requests)
* pytest-xdist (for parallel execution)
* allure-pytest (for reporting)


### **Install the required packages:**
`pip install -r requirements.txt`


### **Configuration**

* **pytest.ini:** Configuration settings for pytest. Customize settings such as markers, log level, and plugins.
* **config.py:** Contains environment-specific settings and API endpoints.


### **Usage**

* #### **Running Tests**

To execute all the tests, run:

`pytest`

To execute all the tests with console logs, run:
`pytest -v -s` 

To execute specific tests with console logs, run:
`pytest <filename> -v -s`

To generate the HTML reports, run:
`pytest --html=report.html`
