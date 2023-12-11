FROM python:3.9-slim

COPY . /app

COPY requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["./entrypoint.sh"]
