FROM python:3.8-alpine
WORKDIR /code
COPY ./ /code/

RUN apk add curl

RUN ls -ltr /code
RUN pip install -r requirements.txt
ENV FLASK_APP ServiceMain.py
CMD flask run --host=0.0.0.0
 