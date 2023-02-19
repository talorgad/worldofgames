FROM python:alpine3.16
RUN mkdir /app
copy MainScores.py /app
copy Scores.txt /app
WORKDIR /app
CMD python MainScores.py