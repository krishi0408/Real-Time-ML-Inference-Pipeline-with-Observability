FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy inference code
COPY inference/ /app/inference/

# Build the ML model inside container
RUN python inference/create_model.py

# Run FastAPI app
CMD ["uvicorn", "inference.api:app", "--host", "0.0.0.0", "--port", "8000"]