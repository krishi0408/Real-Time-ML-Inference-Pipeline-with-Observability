# Creates a FastAPI app.
# Loads a pre-trained Iris classification model from disk.
from fastapi import FastAPI
import joblib
import numpy as np
import time
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response

app = FastAPI()
model = joblib.load('iris_model.pkl')
# counts how many predictions have been requested.
REQUEST_COUNT = Counter("inferece_requests", "Number of inference requests")
# records how long each prediction request takes.
REQUEST_LATENCY = Histogram("inference_request_latency_seconds", "Latency of inference requests in seconds")

# Calls the model’s .predict() method and returns the prediction.
# Increments request count and logs latency into Prometheus metrics.
# Accepts four query parameters (f1, f2, f3, f4) → likely features of the Iris dataset (sepal length, sepal width, petal length, petal width).
@app.get("/predict")
def predict(f1: float, f2:float, f3:float, f4:float):
    start = time.time()
    REQUEST_COUNT.inc()
    pred = model.predict(np.array([[f1,f2,f3,f4]]))[0]
    REQUEST_LATENCY.observe(time.time()-start)
    return {"prediction": int(pred)}

# Returns all collected Prometheus metrics (request count, latency, plus default process/system metrics).
# Used by Prometheus to scrape metrics for monitoring.
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

