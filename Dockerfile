FROM python@sha256:023cdc92b5992ff45c68a2509de0872e5e29329655866fa7bf8f9eeb99834b46

RUN pip install requests

RUN pip install pytest

RUN pip install pytest-xdist

RUN pip install pytest-html

WORKDIR /user/local/

COPY pytest pytest/