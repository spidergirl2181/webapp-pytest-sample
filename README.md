# webapp-pytest-sample

## Pre-requisites
1. Install python version >= 3.6 (Download at: https://www.python.org/downloads/)
2. Install pip on your local machine if you don't have pip pre-installed (Guideline: https://pip.pypa.io/en/stable/installation/)
3. Install other necessary packages (_requests, pytest, pytest-xdist, pytest-html_) via pip:

``` sh
$ pip install -r requirements.txt
```

## How-to: run the sample test

1. Clone this repository to your local machine
2. Standing at root directory: 'webapp-pytest-sample', open terminal/command-line window
3. Run the sample test with logs on console only:

``` sh
$ pytest
```

4. Run the sample test and get test report save at the root directory:

``` sh
$ pytest --html=report.html
```

5. Run the scenarios in parallel:

``` sh
$ pytest -n auto
```

OR: 

``` sh
$ pytest \-n x
```
in which: x is an integer

## Shorthand of environment config

1. Download the sample pytest image from Docker Hub via command:

``` sh
$ docker pull havtt/pytest_sample@sha256:60e93a8c9946c2eca5bf4891ac2310bd2cbcc4b73ccd816abfe6111f959b4c83
```

2. Run the downloaded Docker image via terminal/PS window:

``` sh
$ docker run --name pytest -d havtt/pytest-sample:latest sleep infinity
$ docker exec -it pytest /bin/bash/
```

3. After the terminal commands are remotely executable on running Docker container, try this pytest sample with Pytest commands recommended in "How to: run the sample test".
4. Use command: 
``` sh
$ exit 
```
to terminate the remote connection to the running container

``` sh
$ docker stop pytest
```
to terminate the running container
