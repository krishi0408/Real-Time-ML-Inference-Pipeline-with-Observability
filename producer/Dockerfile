FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy producer code
COPY producer/ /app/producer/

CMD ["python", "producer/producer.py"]