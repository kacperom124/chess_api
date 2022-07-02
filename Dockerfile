FROM python:3.8-slim-buster
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py