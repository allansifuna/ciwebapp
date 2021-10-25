FROM python:3.7
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:80 run:app
