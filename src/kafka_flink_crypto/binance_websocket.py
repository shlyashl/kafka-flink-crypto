import json
import websocket
from logger import log
from kafka_producer import KafkaMessageProducer


class BinanceWebSocket:

    def __init__(self, url):
        self.url = url
        self.ws = None
        self.producer = KafkaMessageProducer(bootstrap_servers="kafka:9092", topic="binance-data")

    def _on_open(self, ws):
        ws.send(json.dumps({
            "method": "SUBSCRIBE",
            "params": ["btcusdt@depth5@100ms"],
            "id": 1
        }))
        log.info("connected")

    def _on_message(self, ws, message):
        data = json.loads(message)
        self.producer.send_message(data)
        log.info(f"{data=}")

    def _on_error(self, ws, error):
        log.error(f"{error=}")

    def _on_close(self, ws, close_status_code, close_msg):
        log.warning(f"connection closed: {close_status_code=}, {close_msg=}")
        self.producer.close()

    def run(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )
        log.info("Starting WebSocket client...")
        self.ws.run_forever()


if __name__ == "__main__":
    socket_url = "wss://stream.binance.com:9443/ws/btcusdt@depth5@1000ms"
    ws_client = BinanceWebSocket(socket_url)
    ws_client.run()
