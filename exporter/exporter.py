from prometheus_client import start_http_server
from gauge import generate_gauges
import logging
import dotenv
import time
import os

dotenv.load_dotenv()

def loop() -> None:
    gauges = generate_gauges()
    while True:
        [gauge.set_value() for gauge in gauges]
        time.sleep(60)


if __name__ == "__main__":
    format = "%(asctime)s %(levelname)s: %(message)s"
    level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(format=format, level=level)

    port = int(os.getenv("EXPORTER_PORT", 8083))
    logging.info(f"Starting web server at port {port}")
    start_http_server(port)
    loop()
