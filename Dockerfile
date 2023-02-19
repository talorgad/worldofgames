FROM python:alpine3.16
RUN mkdir /app
copy MainScores.py /app
copy scores.txt /app
WORKDIR /app
CMD python MainScores.py