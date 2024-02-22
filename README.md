## Project Details:

I developed a hybrid framework from the ground up to explore and verify the functionality of website:entrata.com.
Implemented the Page Object Model pattern, generated reports and logs, captured screenshots upon failures, and aimed to minimize redundancy.

## Table of Contents:
- [Prerequisites](#prerequisites)
- [Automated Test cases](#automated-test-cases)
- [Usage](#usage)

## Prerequisites:
- Requirements: Windows OS
- Must have below applications installed:
    1. Install python and selenium
    2. Install pytest and its plugin:
 
                  pip install pytest  
                  pip show pytest
                  pip install pytest pytest-html

## Automated Test cases:

- Test case 1: Home Page Redirect-
  This test case verifies whether the redirection to the home page works correctly regardless of the current page we are on.
- Test case 2: Hover Solutions Menu-
  This test case hovers over the Solution Menu and verifies whether the length of the options matches exact numbers.
- Test case 3: Invalid Login-
  This test case verifies whether an error message is displayed after entering incorrect credentials for a property manager user.

## Usage:
To execute the Test Automation:
1. Clone the repository.
2. Double-click on the "run.bat" file to run the test cases, or alternatively, navigate to the code directory and execute the "pytest" command.
