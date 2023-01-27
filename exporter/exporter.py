from prometheus_client import start_http_server
from sensor import generate_list
import logging
import time


def loop() -> None:
    sensors = generate_list()
    while True:
        [sensor.set_gauge_value() for sensor in sensors]
        time.sleep(60)


if __name__ == "__main__":
    format = "%(levelname)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG)
    # Start up the server to expose the metrics.
    start_http_server(8083)
    loop()
