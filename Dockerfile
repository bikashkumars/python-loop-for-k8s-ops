FROM python:alpine3.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

EXPOSE 5004

CMD [ "python", "-u","app.py" ]