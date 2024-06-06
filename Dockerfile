FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install requests

ENV SITEURL=novalue

CMD ["python3", "icon.py"]