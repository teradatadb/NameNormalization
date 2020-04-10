FROM python:3.6-slim
RUN apt-get update && \
    pip install --upgrade pi