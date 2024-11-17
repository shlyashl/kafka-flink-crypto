import json
import websocket
from logger import log


class BinanceWebSocket:

    def __init__(self, url):
        self.url = url
        self.ws = None

    def _on_open(self, ws):
        log.info("connected")

    def _on_message(self, ws, message):
        data = json.loads(message)
        log.info(f"{data=}")

    def _on_error(self, ws, error):
        log.error(f"{error=}")

    def _on_close(self, ws, close_status_code, close_msg):
        log.warning(f"connection closed: {close_status_code=}, {close_msg=}")

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
