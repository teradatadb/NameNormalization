FROM python:3.6-slim
RUN apt-get update && \
    pip install --upgrade pip && \
    apt-get install build-essenti