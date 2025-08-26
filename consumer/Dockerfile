FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy consumer code
COPY consumer/ /app/consumer/

CMD ["python", "consumer/consumer.py"]
