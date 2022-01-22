#FROM continuumio/miniconda3:4.10.3
FROM python:3.9
RUN apt-get update

RUN mkdir /JobProject
COPY . /JobProject/
WORKDIR /JobProject/


# install package
RUN pip install pipenv && pipenv sync

# genenv
RUN VERSION=RELEASE python genenv.py

# 預設執行的指令
#CMD ["pipenv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8888"]
#port 80 for traefik load balance
CMD ["pipenv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]