# webapp-pytest-sample

[Pre-requisites]
1. Install python version >= 3.6 (Download at: https://www.python.org/downloads/)
2. Install pip on your local machine if you don't have pip pre-installed (Guideline: https://pip.pypa.io/en/stable/installation/)
3. Install other necessary packages (requests, pytest, pytest-xdist, pytest-html) via pip:

_$ pip install -r requirements.txt_
 
[How-to: run the sample test]

1. Clone this repository to your local machine
2. Standing at root directory: 'webapp-pytest-sample', open terminal/command-line window
3. Run the sample test with logs on console only:

_$ pytest_

4. Run the sample test and get test report save at the root directory:

_$ pytest --html=report.html_

5. Run the scenarios in parallel:

_$ pytest -n auto_

OR: 

_$ pytest \-n x (x is an integer)_

[Shorthand of environment config]

1. Download the sample pytest image from Docker Hub via command:

_$ docker pull havtt/sample-pytest:sample_

2. Run the downloaded Docker image via terminal/PS window:

_$ docker run havtt/sample-pytest:sample_
