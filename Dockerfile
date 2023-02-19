FROM python:alpine3.16
copy MainScores.py /app
copy Scores.txt /app
WORKDIR /app
CMD python MainScores.py