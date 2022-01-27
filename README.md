# webapp-pytest-sample

[Pre-requisites]
1. Install python version >= 3.6 (Download at: https://www.python.org/downloads/)
2. Install pip on your local machine if you don't have pip pre-installed (Guideline: https://pip.pypa.io/en/stable/installation/)
3. Install other necessary packages (requests, pytest, pytest-xdist, pytest-html) via pip:
---
$ pip install -r requirements.txt
---
 
[How-to: run the sample test]

1. Clone this repository to your local machine
2. Standing at root directory: 'webapp-pytest-sample', open terminal/command-line window
3. Run the sample test with logs on console only:
---
$ pytest
---
4. Run the sample test and get test report save at the root directory:
---
$ pytest --html=report.html
---
5. Run the scenarios in parallel:
---
$ pytest -n auto #OR: pytest -n x (x is an integer)
---

[How-to: shortcut an environment config]
TBD
