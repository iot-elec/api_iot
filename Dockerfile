# FROM python:3.11.0a6-alpine3.15
FROM python:3.11.0
WORKDIR /code
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code

CMD ["python3", "app.py"]
# CMD ["gunicorn","--workers", "2", "--timeout", "1000", "--bind", "0.0.0.0:5000", "app:app"]