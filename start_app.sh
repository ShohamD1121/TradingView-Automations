#!/bin/sh

# Set SSL_CERT_FILE to the path of the CA bundle provided by certifi
export SSL_CERT_FILE=$(python -m certifi)

# Start Uvicorn with your FastAPI app
uvicorn main:app --host 0.0.0.0 --port 80 --reload