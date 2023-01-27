from prometheus_client import start_http_server
import logging
import time
import sensor

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)


def loop() -> None:
    sensors = sensor.generate_list()
    while True:
        [sensor.set_gauge_value() for sensor in sensors]
        time.sleep(60)


if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(8083)
    loop()
