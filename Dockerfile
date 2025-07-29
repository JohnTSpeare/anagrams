FROM python:3.11 AS test
ADD . .
RUN pip install mock==5.2.0 pytest==8.3.5 pytest-cov==4.1.0

FROM python:3.11 AS main
ADD . .
