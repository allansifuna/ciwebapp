FROM python:3.7
RUN pip install --upgrade
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
ENTRYPOINT FLASK_APP=run.py flask run
