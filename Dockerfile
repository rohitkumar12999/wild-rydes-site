# Use small official python base
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Use gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app", "--workers", "2"]
