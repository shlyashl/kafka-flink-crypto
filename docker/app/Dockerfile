FROM python:3.12-slim


WORKDIR /app
RUN echo pwd
COPY ./src/kafka_flink_crypto/ /app/

COPY docker/app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "-m", "binance_websocket"]
# CMD ["tail", "-f", "/dev/null"]