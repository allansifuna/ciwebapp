FROM python:3.7
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT FLASK_APP=run.py flask run
